from abc import ABCMeta, abstractmethod

class Observable(metaclass=ABCMeta):
    @abstractmethod
    def update(self, value):
        pass