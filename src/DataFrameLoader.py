from AbstractLoader import Loader
import pandas as pd

class DataFrameLoader(Loader):
    def save(self,dataFrame):
        raise NotImplementedError
    
    def load(self,dataFrame):
        raise NotImplementedError
        
    def load_from_list(self, lista):
        dictionary = {title:column for (title,column) in lista}
        return pd.DataFrame(dictionary)