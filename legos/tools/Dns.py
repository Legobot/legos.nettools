#!/usr/bin/env python

import dns.resolver

from Legobot.Utilities import Utilities as utils
from legos.tools.Tool import ToolScheme

__author__ = "Nitrax <nitrax@lokisec.fr>"
__copyright__ = "Copyright 2017, Legobot"


class Dns(ToolScheme):
    """This class retrieves the DNS record behind a given domain name.
    """

    def __init__(self, args):
        if utils.isNotEmpty(args):
            super().__init__(args)

            self.fncs = {
                'getMX': self._getMX,
            }

    def run(self):
        if utils.isNotEmpty(self.target):
            results = []

            if len(self.cmds) > 0:
                for cmd in self.cmds:
                    try:
                        results.append(self.fncs[cmd]())
                    except KeyError:
                        results.append('Command unknown: ' + cmd)
            else:
                results.append(self._getA())

            return '\n'.join(results)
        else:
            return self.getHelp()

    def _getMX(self):
        """Get MX records

        Args:
            self: self

        Returns:
            str: MX records
        """
        try:
            data = dns.resolver.query(self.target, 'MX')
            results = []
            for item in data:
                results.append(str(item.exchange))
            return ' | '.join(results)
        except:
            return 'Domain name invalid'

    def getHelp(self):
        return "!dns {--getMX} {target}"
