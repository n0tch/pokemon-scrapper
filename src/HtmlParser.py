import requests
from bs4 import BeautifulSoup
from multiprocessing import Process, Manager

class HtmlParser():
    def __init__(self, base_url):
        self.base_url = base_url
        self.all_pokemon_path = 'pokedex/all'
        self.table_id = 'pokedex'
        self.pokemon_list = []
    
    """return html content from given url"""
    def html_content(self, path):
        page = requests.get(self.base_url + path)
        html_doc = BeautifulSoup(page.content, 'html.parser')
        return html_doc

    def content_by_id(self, id):
        html_doc = self.html_content(self.all_pokemon_path)
        table = html_doc.find(id=id)
        return table

    """get elements inside a father link. Gets the content of the 3 first table and append the image link and return it as a tuple"""
    def sub_elements(self, intern_html, id_path):
        img = intern_html.find('div', {'class':'tabs-panel'}).find('img')['src']

        #data elements
        tb_list = [td.find_all('td') for td in intern_html.find_all('table', {'class':'vitals-table'})]
        elements = []
        for tds in tb_list[:3]:
            for td in tds:
                elements.append(td.get_text().strip().replace("\n", ""))

        return (img, elements)

    """get the header of the 3 first table, append with the Image header"""
    def sub_headers(self, intern_html):
        col = []
        th_list = [th.find_all('th') for th in intern_html.find_all('table', {'class':'data-table'})]

        for ths in th_list[:3]:
            for th in ths:
                print(th.get_text().strip().replace('\n', ''))
                col.append((th.get_text().strip().replace('\n', ''), []))

        col.append(('Image', []))
        return col
    
    """append the first line to col and pop it from list"""
    def table_headers(self, html):
        header = html.find_all('tr')
        col = []

        [col.append((h.get_text(),[])) for h in header.pop(0).find_all('div', {'class':'sortwrap'})]
        return col
    
    """return the col of a given table"""
    def columns(self, table):
        return self.table_headers(table)
    
    def elements(self, table):
        rows = table.find_all('tr')
        rows.pop(0)

        #need to find a way to run this func in parallel
        for index, row in enumerate(rows):
            self.extract_data(row, index)
            if index > 10:
                break

        return self.pokemon_list

    def extract_data(self, row, index):
        line = []
        num_pokedex = row.find('td', {'class':'cell-num cell-fixed'}).find('span', {'class':'infocard-cell-data'}).get_text()
        name_pokedex = row.find('a', {'class':'ent-name'}).get_text()
        extended_name = ""
        
        try:
            extended_name = row.find('small', {'class':'aside'}).get_text()
        except:
            pass

        print('Capturando ' + name_pokedex+ ' ' + extended_name + '...')
        types = [types.get_text() for types in row.find_all('a', {'class':'type-icon'})]
        num_total = row.find('td', {'class':'cell-total'}).get_text()
        attrs = [attr.get_text() for attr in row.find_all('td', {'class':'num'})[-6:]]

        line.append(num_pokedex)
        line.append(name_pokedex + ' ' + extended_name)
        line.append(types)
        line.append(num_total)

        for attr in attrs:
            line.append(attr)
        
        self.pokemon_list.append(line)
