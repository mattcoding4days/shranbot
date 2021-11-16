"""
Discord bot actor
"""

import discord
from result import Ok, Err, Result
from shranbot import Config
from shranbot.logging.pkg_logger import Logger
from shranbot.services.tickers.dmgi import Dmgi

Log = Logger().get_logger()


class HerbertWest(discord.Client):
    """
    The actor
    """

    async def guild_name(self) -> Result[str, str]:
        """
        @description: retrieve the guild
        """
        for guild in self.guilds:
            if guild.name == Config.discord_guild():
                return Ok(str(guild.name))

        return Err("No active server was found")

    async def on_ready(self):
        """
        @description: test method
        """
        res = await self.guild_name()
        if res.is_ok():
            Log.info("Bot %s has connected to the %s discord server",
                     self.user, res.value)
        else:
            Log.error("%s", res.value)

    async def on_member_join(self, member):
        """
        @description: Greet new members to the server
        """
        await member.create_dm()
        res = await self.guild_name()
        await member.dm_channel.send(
            f"Hi {member.name}, welcome to the {res.unwrap()} server"
        )

    async def on_message(self, message):
        """
        @description: execute commands from a user
        """
        if message.author == self.user:
            return

        if message.content.startswith("$hello"):
            await message.channel.send("Hello There")

        if message.content.startswith("$dmgi_close"):
            dmgi = Dmgi()
            await message.channel.send(f"{dmgi.todays_closing_price()}")
