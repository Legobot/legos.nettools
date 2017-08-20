from abc import ABCMeta, abstractmethod

class ToolScheme(metaclass=ABCMeta):
    """ToolScheme is an abstract class which should be implemented in any tools
    supported by LegoNettools.
    """
    def __init__(self, args):
        self.cmd = None
        self.target = None

        for arg in args:
            if '--' in arg:
                self.cmd = arg.replace('--', '')
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
