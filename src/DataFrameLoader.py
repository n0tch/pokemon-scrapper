from AbstractLoader import Loader
import pandas as pd

class DataFrameLoader(Loader):
    def save(self, dataFrame):
        pass

    def load(self, pathToLoad):
        pass

    def load_from_list(self, pokemon_list):
        dic = {}
        for (title,column) in pokemon_list:
            if len(column) != 0:
                dic[title] = column

        for key in dic:
            print("{} has {} elements".format(key, len(dic[key])))
        
        return pd.DataFrame(dic)
