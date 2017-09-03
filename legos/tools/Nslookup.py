#!/usr/bin/env python

import re
import socket

from Legobot.Utilities import Utilities as utils
from legos.tools.Tool import ToolScheme

__author__ = "Nitrax <nitrax@lokisec.fr>"
__copyright__ = "Copyright 2017, Legobot"


class Nslookup(ToolScheme):
    """This class allows resolving the IP address from a domain name as well as
       the reverse process.
    """

    def __init__(self, args):
        if utils.isNotEmpty(args):
            super().__init__(args)

    def run(self):
        if utils.isNotEmpty(self.target):
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", self.target):
                return self._getIP()
            else:
                return self._getDomainName()
        else:
            return self.getHelp()

    def _getDomainName(self):
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

    def _getIP(self):
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
        return " !nslookup {target}"
