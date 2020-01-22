from parser.AbstractParser import AbstractParser

class PokemonDetailData(AbstractParser):
    def __init__(self, path):
        super(PokemonDetailData, self).__init__()
        self.path = path
    
    def get_columns(self):
        pass

    def get_elements(self):
        pass

    def load_list(self, max_rows):
        self.html_content(self.path)
