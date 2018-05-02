from Scrapper import *

if __name__ == '__main__':
	url_base = 'https://pokemondb.net'
	scrapper = Scrapper(url_base)
	elements = get_elements()
	element_list = elements_to_list(elements)
	#dataFrame = list_to_dataFrame(element_list)
	#print(dataFrame.head())