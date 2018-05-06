from AbstractLoader import Loader
import pandas as pd

class CsvPokemon(Loader):

    def saveDataFrame(self,dataFrame):
        dataFrame.to_csv('../../data/PokemonData.csv')
    
    def loadDataFrame(self, dataFrame):
        print("Not implemented yet.")