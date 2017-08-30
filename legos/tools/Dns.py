import dns.resolver

from Legobot.Utilities import Utilities as utils
from legos.tools.Tool import ToolScheme

__author__ = "zSec <b1337@zsec.de>"
__copyright__ = "Copyright 2017, Legobot"


class Dns(ToolScheme):
    """The DNS class allows a DNS lookup for various records.
    """

    def __init__(self, args):
        if utils.isNotEmpty(args):
            super().__init__(args)

            self.fncs = {
                'A': self._A,
                'AAAA': self._AAAA,
                'NS': self._NS,
                'MX': self._MX,
                'TXT': self._TXT
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
                results.append(self._A())
                results.append(self._AAAA())
                results.append(self._NS())
                results.append(self._MX())
                results.append(self._TXT())

            return '\n'.join(results)
        else:
            return self.getHelp()

    def _A(self):
        """Get the A record
       Args:
           self: self
           
       Returns:
           str: A Record
       """
       	try:
            data = dns.resolver.query(self.target, 'A')
            results = []
            for item in data:
                results.append(str(item.address))
            return ' | '.join(results)
        except:
            return 'Domain name invalid'

    def _AAAA(self):
        """Get the AAAA record
       Args:
           self: self
           
       Returns:
           str: AAAA record
       """
       	try:
            data = dns.resolver.query(self.target, 'AAAA')
            results = []
            for item in data:
                results.append(str(item.address))
            return ' | '.join(results)
        except:
            return 'Domain name invalid'

    def _NS(self):
        """Get the NS record
       Args:
           self: self
           
       Returns:
           str: NS record
       """
       	try:
            data = dns.resolver.query(self.target, 'NS')
            results = []
            for item in data:
                results.append(str(item.target))
            return ' | '.join(results)
        except:
            return 'Domain name invalid'

    def _MX(self):
        """Get the MX record
       Args:
           self: self
           
       Returns:
           str: MX record
       """
       	try:
            data = dns.resolver.query(self.target, 'MX')
            results = []
            for item in data:
                results.append(str(item.exchange))
            return ' | '.join(results)
        except:
            return 'Domain name invalid'

    def _TXT(self):
        """Get the TXT record
       Args:
           self: self
           
       Returns:
           str: TXT record
       """
       	try:
            data = dns.resolver.query(self.target, 'TXT')
            results = []
            for item in data:
                results.append(str(item.strings))
            return ' | '.join(results)
        except:
            return 'Domain name invalid'

    def getHelp(self):
        return "!dns {--A | --AAAA | " \
               "--NS | --MX | " \
               "--TXT} {target}"
