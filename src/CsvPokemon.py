from AbstractLoader import Loader

class CsvPokemon(Loader):

    def save(self,dataFrame):
        dataFrame.to_csv('../data/PokemonData.csv')
    
    def load(self, dataFrame):
        NotImplementedError