import importlib
import logging

from Legobot.Lego import Lego

logger = logging.getLogger(__name__)


class LegoNettools(Lego):
    """LegoNettols provides support for any networking tools.

    Args:
        Lego: Lego
    """
    @staticmethod
    def listening_for(message):
        """Check if the message contains a command that LegoNettools support.

        Args:
            message: The message send by the Legobot framework

        Returns:
            Bool: Return True if the command is supported
        """
        if message['text'] is not None:
            cmds = ['!whois']
            return message['text'].split()[0] in cmds

    def handle(self, message):
        """Generate and execute the class corresponding to the asked command.

        Args:
            self: self
            message: The message send by the Legobot framework
        """
        tokens = message['text'].split()
        _class = self._factory(tokens[0])

        if ' ' in message['text']:
            if len(tokens) >= 2:
                self.reply(message,  _class(tokens[1:len(tokens)]).run(),
                           self._handle_opts(message))
        else:
            self.reply(message, 'Usage :' + _class(None).getHelp(),
                       self._handle_opts(message))

    def _factory(self, cmd):
        cmd = cmd.replace('!', '')
        _class = cmd.replace(str(cmd[0]), chr(ord(cmd[0]) - 32))

        return getattr(importlib.import_module('legos.tools.' + _class),
                       _class)

    def _handle_opts(self, message):
        """Identify and set the message sourche channel.

        Args:
            self: self
            message: The message send by the Legobot framework

        Returns:
            Array: Options needed to send back the response to the
                Legobot framework
        """
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
        """Get the class name.

        Args:
            self: self

        Returns:
            str: Class name
        """
        return 'nettools'

    @staticmethod
    def get_help():
        """Get helper

        Args:
            self: self

        Returns:
            str: Helper
        """
        help_text = '!whois for further information'

        return help_text
