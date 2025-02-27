from abc import ABCMeta, abstractmethod

class Singleton(object):
    _instance = None
    def __init__(self):
        if self._instance is not None:
            raise ValueError("An instance already exists")
        else:
            self._instance = self
            
    @staticmethod
    def getInstance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance
    
if __name__ == "__main__":
    s1 = Singleton.getInstance()
    s2 = Singleton.getInstance()
    print(s1._instance)
    print(s1 == s2)
    s3 = Singleton()
    print(s1 == s3)