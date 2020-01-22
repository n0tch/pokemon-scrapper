from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup

class AbstractParser(ABC):
    def __init__(self):
        self.base_url = 'https://pokemondb.net/'
        self.all_pokemon_path = 'pokedex/all'
        self.main_table = 'pokedex'
    
    def html_content(self, path):
        page = requests.get(self.base_url + path)
        html_doc = BeautifulSoup(page.content, 'html.parser')
        return html_doc
    
    def content_by_id(self, path, id):
        html_doc = self.html_content(path)
        content = html_doc.find(id=id)
        return content

    @abstractmethod
    def get_columns(self):
        pass

    @abstractmethod
    def get_elements(self):
        pass

    @abstractmethod
    def load_list(self, max_rows=None):
        pass