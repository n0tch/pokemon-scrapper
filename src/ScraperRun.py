import Scraper as Scraper
import pandas as pd
from CsvPokemon import CsvPokemon
from JsonPokemon import JsonPokemon
from DataFrameLoader import DataFrameLoader

if __name__ == '__main__':
    pokemonScraper  = Scraper.PokemonScraper()
    csvLoader       = CsvPokemon()
    jsonLoader      = JsonPokemon()
    dataFrameLoader = DataFrameLoader()

    columns = pokemonScraper.columns()
    rows    = pokemonScraper.elements()

    pokemon_list = pokemonScraper.elements_to_list(columns, rows)
    pokemonDF = dataFrameLoader.load_from_list(pokemon_list)

    print(pokemonDF.head())
    
    csvLoader.save(pokemonDF)
    jsonLoader.save(pokemonDF)
    
    #pokemonDF = pokemonScraper.elements_to_list()