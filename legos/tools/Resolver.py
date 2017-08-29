#!/usr/bin/env python

import socket

from Legobot.Utilities import Utilities as utils
from legos.tools.Tool import ToolScheme

__author__ = "Nitrax <nitrax@lokisec.fr>"
__copyright__ = "Copyright 2017, Legobot"


class Resolver(ToolScheme):
    """This class allows resolving the IP address from a domain name as well as
       the reverse process.
    """

    def __init__(self, args):
        if utils.isNotEmpty(args):
            super().__init__(args)

            self.fncs = {
                'host': self._host,
                'nslookup': self._nslookup
            }

    def run(self):
        if utils.isNotEmpty(self.target):
            if len(self.cmds) > 0:
                for cmd in self.cmds:
                    try:
                        return self.fncs[cmd]()
                    except KeyError:
                        return 'Command unknown: ' + cmd
        else:
            return self.getHelp()

    def _host(self):
        """Retrieve the IP address corresponding to a domain name.

        Args:
            self: self

        Returns:
            str: IP address
        """
        try:
            return socket.gethostbyname(self.target)
        except:
            return 'Host cannot be resolved'

    def _nslookup(self):
        """Retrieve the domain name corresponding to an IP address.

        Args:
            self: self

        Returns:
            str: domain name
        """
        try:
            return socket.gethostbyaddr(self.target)[0]
        except:
            return 'IP address cannot be resolved'

    def getHelp(self):
        return " !resolver {--host | --nslookup} {target}"
