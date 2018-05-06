from src.service.AbstractLoader import Loader
import pandas as pd

class JsonPokemon(Loader):

    def saveDataFrame(self, dataFrame):
        dataFrame.to_json('../../data/PokemonData.json')

    def loadDataFrame(self, pathToLoad):
        print("Not implemented yet.")
