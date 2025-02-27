from abc import ABCMeta, abstractmethod

class RegisterUserAbc(metaclass=ABCMeta):
    @abstractmethod
    def register(self):
        pass
    
    @abstractmethod
    def login(self):
        pass