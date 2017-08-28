#!/usr/bin/env python

import json
import urllib3

from Legobot.Utilities import Utilities
from legos.tools.Tool import ToolScheme

__author__ = "Nitrax <nitrax@lokisec.fr>"
__copyright__ = "Copyright 2017, Legobot"


class Geoloc(ToolScheme):
    """The Geoloc class allows retrieve the lat/long of a given IP address.
    """

    def __init__(self, args):
        if Utilities.isNotEmpty(args):
            super().__init__(args)

    def run(self):
        if self.target is not None:
            return self._getInfo('http://freegeoip.net/json/')
        else:
            return self.getHelp()

    def _getInfo(self, url):
        """Geoloc the given IP address.

        Args:
            self: self
            url: Geoloc service

        Returns:
            str: IP information
        """

        http = urllib3.PoolManager()

        res = http.request('GET', url + self.target)
        try:
            content = json.loads(res.data.decode('utf-8'))

            return content['country_name'] + ' [' \
                + content['country_code'] + ']' \
                + ' --- ' + content['city'] + ' {' \
                + str(content['longitude']) \
                + ' - ' + str(content['latitude']) + '}'
        except:
            return 'Geolocalisation failed'

    def getHelp(self):
        return "!geoloc {target}"
