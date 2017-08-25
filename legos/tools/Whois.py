#!/usr/bin/env python

import whois

from Legobot.Utilities import Utilities as utils
from legos.tools.Tool import ToolScheme

__author__ = "Nitrax <nitrax@lokisec.fr>"
__copyright__ = "Copyright 2017, Legobot"


class Whois(ToolScheme):
    """The Whois class wrappes the whois linux binary.
    """
    def __init__(self, args):
        if utils.isNotEmpty(args):
            super().__init__(args)

            self.fncs = {
                'getRegistrar': self._getRegistrar,
                'getNS': self._getNS,
                'getEmails': self._getEmails,
                'getStatus': self._getStatus
            }

    def run(self):
        if utils.isNotEmpty(self.target):
            data = whois.whois(self.target)
            results = []

            if len(self.cmds) > 0:
                for cmd in self.cmds:
                    try:
                        results.append(self.fncs[cmd](data))
                    except KeyError:
                        results.append('Command unknown: ' + cmd)
            else:
                results.append(self._getRegistrar(data))
                results.append(self._getNS(data))
                results.append(self._getEmails(data))
                results.append(self._getStatus(data))

            return '\n'.join(results)
        else:
            return self.getHelp()

    def _getRegistrar(self, data):
        """Get the target registrar

        Args:
            self: self
            data: Whois results

        Returns:
            str: Registrar
        """
        return data.registrar if utils.isNotEmpty(data.registrar) else 'None'

    def _getNS(self, data):
        """Get the target name servers

        Args:
            self: self
            data: Whois results

        Returns:
            str: Name servers
        """
        ns = data.name_servers
        return ' - '.join(ns) if utils.isNotEmpty(ns)else 'None'

    def _getStatus(self, data):
        """Get the target status

        Args:
            self: self
            data: Whois results

        Returns:
            str: Status
        """
        return data.status[1] if utils.isNotEmpty(data.status) else 'None'

    def _getEmails(self, data):
        """Get the target emails

        Args:
            self: self
            data: Whois results

        Returns:
            str: Emails
        """

        if utils.isNotEmpty(data.emails):
            return ' - '.join(data.emails)
        else:
            return 'None'

    def getHelp(self):
        return "!whois {--getRegistrar | --getNS |" \
            "--getEmails | --getStatus} {target}"
