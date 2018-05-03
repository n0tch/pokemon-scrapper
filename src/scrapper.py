import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

class Scrapper(object):
	def __init__(self, base_url):
		"""Basic vars for init a scrapper object"""
		self.base_url = base_url
		self.elemets = []

	def get_elements(self):
		"""given a html_element, returns the elements within that element in the page"""
		html_doc = self.get_html_content('/pokedex/all')

		table = html_doc.find(id='pokedex')
		return table

	def get_sub_elements(self,html_doc):
		""" get elements inside a father link. Gets the content of the 3 first tables, append the image link and return as a tuple"""
		img = html_doc.find('div',{'class':'figure'}).find('img')['src']

		td_list = [td.find_all('td') for td in html_doc.find_all('table',{'class':'vitals-table'})]
		lista = []
		for tds in td_list[:3]:
			for td in tds:
				lista.append(td.get_text().strip().replace("\n",""))


		return (img,lista)

	def get_sub_headers(self, html_doc):
		""" get the header of the 3 first tables, appending with the 'Image' header."""
		col = []
		th_list = [th.find_all('th') for th in html_doc.find_all('table',{'class':'vitals-table'})]

		for ths in th_list[:3]:
			for th in ths:
				col.append((th.get_text().strip().replace("\n",""),[]))

		col.append(("Image",[]))		
		return col

	def get_html_content(self, url):
		""" generic function to return the content of the given url"""
		page = requests.get(self.base_url + '/' + url)
		html_doc = bs(page.content, 'html.parser')

		return html_doc

	def elements_to_list(self, elements):
		"""insert given elements to a list and returns that list"""
		rows = elements.find_all('tr')

		col = []

		#read and pop the first line of the table
		[col.append((header.get_text(),[])) for header in rows.pop(0).find_all('div', {'class':"sortwrap"})]

		#reading the rest of the contents
		for row in rows:
			line = []
			num_pokedex = row.find('td', {'class':'cell-icon-string'}).get_text().strip()
			name_pokedex = row.find('a',{'class':'ent-name'}).get_text()
			extended_name = "" 

			try:
				extended_name = " " + row.find('small',{'class':'aside'}).get_text()
			except:
				pass

			link = row.find('a',{'class':'ent-name'})['href']
			sub_link = self.base_url + link
			types = [types.get_text() for types in row.find_all('a',{'class':'type-icon'})]
			num_total = row.find('td', {'class':'num-total'}).get_text()
			attrs = [attr.get_text() for attr in row.find_all('td',{'class':'num'})[-6:]]

			intern_html_doc = self.get_html_content(sub_link)			
			if len(col) <= 10:
				for c in self.get_sub_headers(intern_html_doc):
					col.append(c)

			sub_elements = self.get_sub_elements(intern_html_doc)

			line.append(num_pokedex)
			line.append(name_pokedex+extended_name)
			line.append(types)
			line.append(num_total)

			for attr in attrs:
				line.append(attr)

			for element in sub_elements[1]:
				line.append(element)

			line.append(sub_elements[0])

			print("Capiturando " + name_pokedex+extended_name + '...')
			#Qubrar codigo aqui.
			if len(line) != len(col):
				line.insert(18,"")

			i = 0
			#matchs the lines with the columns
			for l in line:
				col[i][1].append(l)
				i+=1

		return col

	def list_to_dataFrame(self, lista):
		""" get a list and return a dataframe with that content """
		Dict = {title:column for (title,column) in lista}
		df = pd.DataFrame(Dict)
		return df

	def dataFameToJson(self, dataFrame):
		""" write dataframe as a json file"""
		dataFrame.to_json('../data/PokemonData.json')

	def dataFrameToCsv(self,dataFrame):
		""" write dataframe as a csv file, separated by ',' """
		dataFrame.to_csv('../data/PokemonData.csv', sep=',', encoding='utf-8')

	def str_bracket(word):
	    '''Add brackets around second term'''
	    list = [x for x in word]
	    for char_ind in range(1, len(list)):
	        if list[char_ind].isupper():
	            list[char_ind] = ' ' + list[char_ind]
	    fin_list = ''.join(list).split(' ')
	    length = len(fin_list)
	    if length>1:
	        fin_list.insert(1,'(')
	        fin_list.append(')')
	    return ' '.join(fin_list)

	    
	def str_break(word):
	    '''Break strings at upper case'''
	    list = [x for x in word]
	    for char_ind in range(1, len(list)):
	        if list[char_ind].isupper():
	            list[char_ind] = ' ' + list[char_ind]
	    fin_list = ''.join(list).split(' ')
	    return fin_list

if __name__ == '__main__':
	url_base = 'https://pokemondb.net'
	scrapper = Scrapper(url_base)
	elements = scrapper.get_elements()
	element_list = scrapper.elements_to_list(elements)
	dataFrame = scrapper.list_to_dataFrame(element_list)
	scrapper.dataFameToJson(dataFrame)

	print(dataFrame.head())
