#!/usr/bin/env python

from legos.libs.ICMP import ping
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
            try:
                ping.Ping(self.target, 4242, 1, 0, 64, 2).run()
                return "Host is up"
            except:
                return "Host is down"
        else:
            return self.getHelp()

    def getHelp(self):
        return "!ping {target}"
