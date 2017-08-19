import importlib
import logging

from Legobot.Lego import Lego

logger = logging.getLogger(__name__)


class LegoNettools(Lego):
    @staticmethod
    def listening_for(message):
        if message['text'] is not None:
            return message['text'].startswith('!whois')

    def handle(self, message):
        tokens = message['text'].split()
        _class = self._factory(tokens[0])

        if ' ' in message['text']:
            if len(tokens) >= 2:
                _class(tokens[1:len(tokens)]).run()
                # self.reply(message, _class(tokens[1:len(tokens)]).run(), self._handle_opts(message))
        else:
            self.reply(message, 'Usage :' + _class(None).getHelp(),
                self._handle_opts(message))

    def _factory(self, cmd):
        cmd = cmd.replace('!', '')
        _class = cmd.replace(str(cmd[0]), chr(ord(cmd[0]) - 32))

        return getattr(importlib.import_module('legos.tools.' + _class), _class)

    def _handle_opts(self, message):
        try:
            target = message['metadata']['source_channel']
            opts = {'target': target}
        except IndexError:
            opts = None
            logger.error('''Could not identify message source in message:
                                    {}'''.format(str(message)))

        return opts

    @staticmethod
    def get_name():
        return '!whois'

    @staticmethod
    def get_help():
        help_text = '!whois {target}'

        return help_text
