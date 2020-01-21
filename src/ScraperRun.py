import Scraper as Scraper
from DataFrameLoader import DataFrameLoader
from CsvPokemon import CsvLoader

if __name__ == "__main__":
    pokemonScrapper  = Scraper.PokemonScrapper()
    dataFrameLoader  = DataFrameLoader()
    csvLoader        = CsvLoader()

    columns = pokemonScrapper.columns()
    rows    = pokemonScrapper.elements()    

    pokemon_list = pokemonScrapper.elements_to_list(columns, rows)
    pokemon_df = dataFrameLoader.load_from_list(pokemon_list)
    csvLoader.save(pokemon_df)
    print(pokemon_df)

