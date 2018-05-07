import requests
from bs4 import BeautifulSoup
import multiprocessing as mp

class HtmlParser():
    def __init__(self, base_url):
        self.base_url = base_url
        self.all_pokemon_url = '/pokedex/all'
        #self.elements = []
        #self.sub_elements = []
    
    def html_content(self, url):
        """ generic function to return the content of the given url"""
        page = requests.get(self.base_url + '/' + url)
        html_doc = BeautifulSoup(page.content, 'html.parser')

        return html_doc

    def table_content(self):
        html_doc = self.html_content(self.all_pokemon_url)
        table = html_doc.find(id='pokedex')
        return table

    def sub_elements(self,intern_html):
        """ get elements inside a father link. Gets the content of the 3 first tables, append the image link and return as a tuple"""
        img = intern_html.find('div',{'class':'figure'}).find('img')['src']
        
        #table data elements
        td_list = [td.find_all('td') for td in intern_html.find_all('table', {'class':'vitals-table'})]
        elements = []
        for tds in td_list[:3]:
            for td in tds:
                elements.append(td.get_text().strip().replace("\n",""))
        
        return (img, elements)
    
    def sub_headers(self,intern_html):
        """ get the header of the 3 first tables, appending with the 'Image' header."""
        col = []
        th_list = [th.find_all('th') for th in intern_html.find_all('table',{'class':'vitals-table'})]

        for ths in th_list[:3]:
            for th in ths:
                col.append((th.get_text().strip().replace('\n',''),[]))
            
        col.append(('Image',[]))
        return col
    
    def table_headers(self, html):
        header = html.find_all('tr')
        col = []

        #append the first line to col var and pop it from the list
        [col.append((h.get_text(),[])) for h in header.pop(0).find_all('div', {'class':"sortwrap"})]
        return col

    def columns(self, table):
        col = self.table_headers(table)
        sub_link = table.find('a',{'class','ent-name'})['href']
        
        for c in self.sub_headers(self.html_content(sub_link)):
            col.append(c)

        return col

    def elements(self,table):
        rows = table.find_all('tr')
        #pop the first line, because its the header line.
        rows.pop(0)
        
        manager = mp.Manager()
        lines = []
        try:
            with mp.Manager() as manager:
                l = manager.list()
                jobs = []
                i = 0
                for row in rows:
                    
                    p = mp.Process(target=self.extract_data, args=(row,l))
                    p.start()
                    jobs.append(p)

                    if i % 4 == 0:
                        for proc in jobs:
                            proc.join()
                        
                        for elem in l:
                            lines.append(elem)

                    i+=1
        except FileNotFoundError as e:
            pass
            
            
        #print(lines[:])
        return lines
    
    def extract_data(self, row, lines):
        line = []
        num_pokedex = row.find('td', {'class':'num cell-icon-string'}).get_text()
        name_pokedex = row.find('a',{'class':'ent-name'}).get_text()
        extended_name = "" 

        try:
            extended_name = " " + row.find('small',{'class':'aside'}).get_text()
        except:
            pass
        print("Capiturando " + name_pokedex+extended_name + '...')
        link = row.find('a',{'class':'ent-name'})['href']
        sub_link = self.base_url + link
        types = [types.get_text() for types in row.find_all('a',{'class':'type-icon'})]
        num_total = row.find('td', {'class':'num-total'}).get_text()
        attrs = [attr.get_text() for attr in row.find_all('td',{'class':'num'})[-6:]]

        intern_html_doc = self.html_content(sub_link)			

        sub_elements = self.sub_elements(intern_html_doc)

        line.append(num_pokedex)
        line.append(name_pokedex+extended_name)
        line.append(types)
        line.append(num_total)

        for attr in attrs:
            line.append(attr)

        for element in sub_elements[1]:
            line.append(element)

        line.append(sub_elements[0])

        #tenho que ter certeza de que existem 27 colunas nas linhas
        #pois estou pegando exatamente 28 elementos
        #coluna 'Japonese' pode esta faltando(coluna 18).
        #por isso insiro na coluna 18.
        if len(line) != 27:
            line.insert(18,"")

        lines.append(line)
