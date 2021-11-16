"""
Discord bot actor
"""

import discord
from result import Ok, Err, Result
from shranbot import Config
from shranbot.logging.pkg_logger import Logger

Log = Logger().get_logger()


class HerbertWest(discord.Client):
    """
    The actor
    """

    async def guild_name(self) -> Result[str, str]:
        """
        @description: retrieve the guild name
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
            Log.info("Logged on as %s in server %s", self.user, res.value)
        else:
            Log.error("%s", res.value)
