from abc import ABC, abstractmethod

class Loader(ABC):

    @abstractmethod
    def save(self, dataFrame):
        pass

    @abstractmethod
    def load(self, pathToLoad):
        pass