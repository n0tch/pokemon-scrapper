from abc import ABC, abstractmethod
import os

class Loader(ABC):
    @abstractmethod
    def save(self, dataFrame):
        pass

    @abstractmethod
    def load(self, pathToLoad):
        pass

    def createFileIfNotExist(self, dirPath, fileName):
        if not os.path.exists(dirPath):
            os.mkdir(dirPath)