"""
Get the dmgi price data from yahoo finance
"""

import yfinance as yf
from shranbot.utils import Emoji


class Dmgi:
    """
    @description: Encapsulate all DMGI stock related data
    """

    def __init__(self):
        self._ticker = yf.Ticker("DMGI.V")

    def close(self) -> float:
        """
        @description: return todays closing price
        """
        return round(float(self._ticker.history(period='1d')['Close'][0]), 2)

    def open(self) -> float:
        """
        @description: return todays opening price
        """
        return round(float(self._ticker.history(period='1d')['Open'][0]), 2)

    def todays_info(self) -> str:
        """
        @description: display todays performance, if dmgi dropped in value,
         display an emoji chart portraying a downwards trend, else display
         an upwards trending chert
        """
        if self.open() > self.close():
            return "{} ${:0.2f} {}".format(str(Emoji.DOWN), self.close(), Emoji.CAD)

        return "{} ${:0.2f} {}".format(Emoji.UP, self.close(), Emoji.CAD)

    def history(self) -> str:
        """
        @description: test method to see if the discord bot can display table data
        """
        return str(self._ticker.history(period='max'))
