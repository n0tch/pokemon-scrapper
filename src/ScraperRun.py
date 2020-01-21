from loader.DataFrameLoader import DataFrameLoader
from loader.CsvPokemon import CsvLoader
from parser.PokemonMainParser import PokemonMainData
from parser.PokemonDetailParser import PokemonDetailData

if __name__ == "__main__":
    dataFrameLoader   = DataFrameLoader()
    csvLoader         = CsvLoader()
    pokemonMainData   = PokemonMainData()
    pokemonDetailData = PokemonDetailData()

    main_list = pokemonMainData.load_list(max_rows = 1028)

    pokemon_df = dataFrameLoader.build_dataframe(main_list[0], main_list[1])
    csvLoader.save(pokemon_df)
    print(pokemon_df)

