"""
Arb doc
"""

import discord
from shranbot import Config
from shranbot.logging.pkg_logger import Logger

Log = Logger().get_logger()


class HerbertWest(discord.Client):
    """
    The actor
    """

    async def on_ready(self):
        """
        @description: test method
        """
        active_guild = None
        for guild in self.guilds:
            if guild.name == Config.discord_guild():
                active_guild = guild.name
                break

        Log.info("Logged on as %s in server %s", self.user, active_guild)
