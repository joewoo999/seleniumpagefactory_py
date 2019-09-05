import abc


class Command(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, locator, *args):
        pass


class Click(Command):

    def execute(self, locator, *args):
        pass


class Commands:
    pass
