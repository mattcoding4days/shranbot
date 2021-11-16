"""
Example Driver code
"""
# standard lib

# package
from shranbot import Config
from shranbot.services.bot import HerbertWest
# from shranbot.services.tickers.dmgi import Dmgi


def run() -> None:
    """
    Example function to execute through poetry scripts
    """
    herbert = HerbertWest()
    herbert.run(Config.discord_token())
