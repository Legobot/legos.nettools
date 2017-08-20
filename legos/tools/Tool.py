#!/usr/bin/env python

__author__      = "Nitrax <nitrax@lokisec.fr>"
__copyright__   = "Copyright 2017, Legobot"

from abc import ABCMeta, abstractmethod


class ToolScheme(metaclass=ABCMeta):
    """ToolScheme is an abstract class which should be implemented in any tools
    supported by LegoNettools.
    """
    def __init__(self, args):
        self.cmds = []
        self.target = None

        for arg in args:
            if '--' in arg:
                self.cmds.append(arg.replace('--', ''))
            else:
                self.target = arg

    @abstractmethod
    def run(self):
        """Tool entry point.

        Args:
            self: self
        """
        pass

    @abstractmethod
    def getHelp(self):
        """Tool helper.

        Args:
            self: self
        """
        pass
