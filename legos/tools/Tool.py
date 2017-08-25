#!/usr/bin/env python

# from abc import ABCMeta, abstractmethod

import abc

__author__ = "Nitrax <nitrax@lokisec.fr>"
__copyright__ = "Copyright 2017, Legobot"

ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()})


class ToolScheme(ABC):
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

    @abc.abstractmethod
    def run(self):
        """Tool entry point.

        Args:
            self: self
        """
        pass

    @abc.abstractmethod
    def getHelp(self):
        """Tool helper.

        Args:
            self: self
        """
        pass
