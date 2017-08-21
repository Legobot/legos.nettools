#!/usr/bin/env python

from os import system as system_call
from platform import system as system_name

from legos.tools.Tool import ToolScheme

__author__ = "Nitrax <nitrax@lokisec.fr>"
__copyright__ = "Copyright 2017, Legobot"


class Ping(ToolScheme):
    """This class allow to identify if a given target is up or down.
    """
    def __init__(self, args):
        if args is not None:
            super().__init__(args)

    def run(self):
        if self.target is not None:
            p = "-n 1" if system_name().lower() == "windows" else "-c 1"
            r = system_call("ping " + p + " " + self.target
                            + " > /dev/null 2>&1")

            return "Host is up" if r == 0 else "Host is down"
        else:
            return self.getHelp()

    def getHelp(self):
        return "!ping {target}"
