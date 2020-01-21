import Scraper as Scraper
from DataFrameLoader import DataFrameLoader
from CsvLoader import CsvLoader

if __name__ == "__main__":
    pokemonScrapper  = Scrapper.PokemonScrapper()
    dataFrameLoader  = DataFrameLoader()
    csvLoader        = CsvLoader()

    columns = pokemonScrapper.columns()
    rows    = pokemonScrapper.elements()    

    pokemon_list = pokemonScrapper.elements_to_list(columns, rows)
    pokemon_df = dataFrameLoader.load_from_list(pokemon_list)
    csvLoader.save(pokemon_df)
    print(pokemon_df)

