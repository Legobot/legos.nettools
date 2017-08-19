from abc import ABCMeta, abstractmethod

class ToolScheme(metaclass=ABCMeta):

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
        pass

    @abstractmethod
    def getHelp(self):
        pass
