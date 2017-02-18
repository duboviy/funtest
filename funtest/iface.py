from abc import ABCMeta, abstractmethod


class AbstractCommandExecutor(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self, cmd, ret_code):
        """For example, run command with args, return stdout merged with stderr. """
        pass

    @abstractmethod
    def cd(self, arg):
        pass

    @abstractmethod
    def get_cwd(self):
        pass

    @abstractmethod
    def mkdir(self, arg):
        pass

    @abstractmethod
    def full_name(self, fname):
        pass

    @abstractmethod
    def rmtree(self):
        pass

    @abstractmethod
    def read(self, fname):
        pass

    @abstractmethod
    def write(self, fname, text):
        pass
