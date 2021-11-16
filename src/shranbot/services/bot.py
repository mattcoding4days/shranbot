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
        active_guild = Err("No active server was found")
        for guild in self.guilds:
            if guild.name == Config.discord_guild():
                active_guild = Ok(str(guild.name))
                break

        return active_guild

    async def on_ready(self):
        """
        @description: test method
        """
        gname = await self.guild_name()
        if gname.is_ok():
            Log.info("Logged on as %s in server %s", self.user, gname.value)
        else:
            Log.error("%s", gname.value)
