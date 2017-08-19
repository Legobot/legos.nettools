import whois

from legos.tools.Tool import ToolScheme

class Whois(ToolScheme):

    def __init__(self, args):
        if args is not None:
            super().__init__(args)

            self.fncs = {
                'getRegistrar' : self._getRegistrar,
                'getNS' : self._getNS
            }

    def run(self):
        data = whois.whois(self.target)
        print(self.fncs[self.cmd](data))

    def _getRegistrar(self, data):
        return data.registrar

    def _getNS(self, data):
        return  ' - '.join(data.name_servers)

    def getHelp(self):
        return "!whois {target}"

    #nslookup / sslscan / ping / trace / nslookup / dns / geoloc
