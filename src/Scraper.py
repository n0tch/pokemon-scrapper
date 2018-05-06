import requests
from bs4 import BeautifulSoup
import multiprocessing as multiproc
import HtmlParser as html

class PokemonScraper(object):
    def __init__(self):
        self.base_url      = 'https://pokemondb.net'
        self.html_parser   = html.HtmlParser(self.base_url)
        self.table_content = self.html_parser.table_content()
    
    def elements(self):
        return self.html_parser.elements(self.table_content)

    def columns(self):
        return self.html_parser.columns(self.table_content)

    def elements_to_list(self,columns,elements):
        
        for element in elements:
            i = 0
            for e in element:
                columns[i][1].append(e)
                i+=1

        return columns