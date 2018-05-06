import Scraper as Scraper
#from CsvPokemon import CsvPokemon
#from JsonPokemon import JsonPokemon

if __name__ == '__main__':
    pokemonScraper = Scraper.PokemonScraper()
    #csvLoader = CsvPokemon()
    #jsonLoader = JsonPokemon()

    columns = pokemonScraper.columns()
    rows    = pokemonScraper.elements()

    dataFrame_list = pokemonScraper.elements_to_list(columns, rows)

    print(dataFrame_list)
    #pokemonDF = pokemonScraper.elements_to_list()