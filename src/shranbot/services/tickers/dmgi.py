"""
Get the dmgi price data from yahoo finance
"""


import yfinance as yf
import emoji


class Dmgi:
    def __init__(self):
        self.dmgi = yf.Ticker("DMGI.V")

    def todays_closing_price(self) -> str:
        """
        @description: get the current closing price of dmgi
        """
        todays_data = self.dmgi.history(period='1d')
        return "DMGI closed at {}{:0.2f} CAD".format(emoji.emojize(":heavy_dollar_sign:"), todays_data['Close'][0])
