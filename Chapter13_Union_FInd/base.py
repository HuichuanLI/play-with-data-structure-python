import abc


class UF(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def is_connected(self, p, q):
        raise NotImplementedError

    @abc.abstractmethod
    def union_elements(self, p, q):
        raise NotImplementedError

    @abc.abstractmethod
    def get_size(self):
        raise NotImplementedError
