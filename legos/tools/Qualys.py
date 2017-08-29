#!/usr/bin/env python

import json
import urllib3
import time

from Legobot.Utilities import Utilities as utils
from legos.tools.Tool import ToolScheme

__author__ = "Nitrax <nitrax@lokisec.fr>"
__copyright__ = "Copyright 2017, Legobot"

urllib3.disable_warnings()
http = urllib3.PoolManager()


class Qualys(ToolScheme):
    """The Qualys class allows performing SSL assessment on a given target.
    """

    def __init__(self, args):
        if utils.isNotEmpty(args):
            super().__init__(args)

            self.URL = 'https://api.ssllabs.com/api/v2/'

    def run(self):
        if utils.isNotEmpty(self.target):
            self._initiateRequest()
            return self._getInfo(self._checkStatus())
        else:
            return self.getHelp()

    def _initiateRequest(self):
        """Intentiate the Assessment.

        Args:
            self: self
        """
        http.request('GET', self.URL + '/analyze?host=' + self.target)

    def _getInfo(self, data):
        """Get assessment information.

        Args:
            self: self
            data: Assessment information

        Results:
            str: Results
        """
        if utils.isNotEmpty(data):
            r = http.request('GET', self.URL + '/getEndpointData?host='
                             + self.target + '&s=' + data[0]['ipAddress'])
            data = json.loads(r.data.decode('utf-8'))

            drown = str(data['details']['drownVulnerable'])
            heartbleed = str(data['details']['heartbleed'])
            poodle = str(data['details']['poodle'])

            return '[' + data['grade'] + '] {' + self.target + ' | ' \
                + data['ipAddress'] + '}\n' \
                + 'Vulnerable to drown: [' + drown + ']\n' \
                + 'Vulnerable to heartbleed: [' + heartbleed + ']\n' \
                + 'Vulnerable to poodle: [' + poodle + ']\n'
        else:
            return 'Assessment failed'

    def _checkStatus(self):
        """Check if the analyze is done.

        Args:
            self:self

        Results:
            json: Data
        """
        while True:
            r = http.request('GET', self.URL + '/analyze?host=' + self.target)

            status = json.loads(r.data.decode('utf-8'))['status']
            if status == 'READY':
                return json.loads(r.data.decode('utf-8'))['endpoints']
            elif status == 'ERROR':
                return None

            time.sleep(20)

    def getHelp(self):
        return " !qualys {target}"
