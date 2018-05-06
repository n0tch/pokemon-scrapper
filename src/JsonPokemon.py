from AbstractLoader import Loader

class JsonPokemon(Loader):

    def save(self, dataFrame):
        dataFrame.to_json('../data/PokemonData.json')

    def load(self, pathToLoad):
        NotImplementedError
