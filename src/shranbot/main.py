"""
Example Driver code
"""
# standard lib

# package
from shranbot import Config
from shranbot.services.bot import HerbertWest
from shranbot.logging.pkg_logger import Logger

Log = Logger().get_logger()


def run() -> None:
    """
    Example function to execute through poetry scripts
    """
    herbert = HerbertWest()
    herbert.run(Config.discord_token())
