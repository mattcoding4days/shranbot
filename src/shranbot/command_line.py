"""
command line arguments for this app
"""

import argparse

from shranbot import ThreadSafeMeta, Config


class Cli(metaclass=ThreadSafeMeta):
    """
    @description: App specific aruments go here
    """

    def __init__(self):
        self.__parser = argparse.ArgumentParser(
            prog=Config.package(),
            usage="%(prog)s [options]",
            description="Discord bot",
            allow_abbrev=False,
        )
        self.__parser.add_argument(
            "-r",
            "--run",
            action="store_true"
        )

        # add more arguments here
        self.args = self.__parser.parse_args()
