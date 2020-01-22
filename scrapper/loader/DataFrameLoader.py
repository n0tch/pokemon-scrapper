from loader.AbstractLoader import Loader
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
        
        return pd.DataFrame(dic)
    
    def build_dataframe(self, header, elements):
        for element in elements:
            i = 0
            for e in element:
                header[i][1].append(e)
                i += 1
        return self.load_from_list(header)
