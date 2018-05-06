from abc import ABC, abstractmethod

class Loader(ABC):

    @abstractmethod
    def saveDataFrame(self, dataFrame):
        pass

    @abstractmethod
    def loadDataFrame(self, pathToLoad):
        pass