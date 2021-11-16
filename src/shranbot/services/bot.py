"""
Arb doc
"""

import discord
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
        Log.info("Logged on as %s", self.user)
