from AbstractLoader import Loader
import os

class CsvLoader(Loader):
    def __init__(self):
        self.file_name = 'pokemonData.csv'
        self.dir_path = '../data'

    def save(self, dataFrame):
        self.createFileIfNotExist(self.dir_path, self.file_name)
        print(r'{}'.format(self.dir_path + '/' + self.file_name))
        dataFrame.to_csv(r'{}'.format(self.file_name), sep="\t", index=False)
    
    def load(self, pathToLoad):
        NotImplementedError
