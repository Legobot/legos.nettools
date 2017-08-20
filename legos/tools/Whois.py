import whois

from legos.tools.Tool import ToolScheme


class Whois(ToolScheme):
    """The Whois class wrappes the whois linux binary.
    """
    def __init__(self, args):
        if args is not None:
            super().__init__(args)

            self.fncs = {
                'getRegistrar': self._getRegistrar,
                'getNS': self._getNS,
                'getEmails': self._getEmails,
                'getStatus': self._getStatus
            }

    def run(self):
        data = whois.whois(self.target)
        results = []

        if len(self.cmds) > 0:
            for cmd in self.cmds:
                results.append(self.fncs[cmd](data))
        else:
            results.append(self._getRegistrar(data))
            results.append(self._getNS(data))
            results.append(self._getEmails(data))
            results.append(self._getStatus(data))

        return '\n'.join(results)

    def _getRegistrar(self, data):
        """Get the target registrar

        Args:
            self: self
            data: Whois results

        Returns:
            str: Registrar
        """
        return data.registrar

    def _getNS(self, data):
        """Get the target name servers

        Args:
            self: self
            data: Whois results

        Returns:
            str: Name servers
        """
        return ' - '.join(data.name_servers)

    def _getStatus(self, data):
        """Get the target status

        Args:
            self: self
            data: Whois results

        Returns:
            str: Status
        """
        return data.status[1]

    def _getEmails(self, data):
        """Get the target emails

        Args:
            self: self
            data: Whois results

        Returns:
            str: Emails
        """
        return ' - '.join(data.emails)

    def getHelp(self):
        return "!whois {--getRegistrar | --getNS |" \
            "--getEmails | --getStatus} {target}"
