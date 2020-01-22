from parser.AbstractParser import AbstractParser

class PokemonMainData(AbstractParser):
    def __init__(self):
        super(PokemonMainData,self).__init__()

    def load_list(self, max_rows = None):
        columns = self.get_columns()
        rows = self.get_elements(max_rows)
        return (columns, rows)
        
    def get_columns(self):
        feature_list = ['#', 'Name', 'Type', 'Total', 'Link', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
        return [(feature,[]) for feature in feature_list]

    def get_elements(self, num_rows):
        raw_data = self.content_by_id(self.all_pokemon_path, self.main_table)
        rows = raw_data.find_all('tr')
        rows.pop(0)
        feature_list = []
        if num_rows == None:
            num_rows = len(rows)

        for index, element in enumerate(rows):
            if index < num_rows:
                feature_list.append(self.extract_data(element))
            
        return feature_list

    def extract_data(self, element):
        num_pokedex = element.find('td', {'class':'cell-num cell-fixed'}).find('span', {'class':'infocard-cell-data'}).get_text()
        name_pokedex = element.find('a', {'class':'ent-name'}).get_text()
        num_total = element.find('td', {'class':'cell-total'}).get_text()
        types = [types.get_text() for types in element.find_all('a', {'class':'type-icon'})]
        link = element.find('a',{'class':'ent-name'})['href']
        attrs = element.find_all('td', {'class':'cell-num'})[1:]

        return_list = [num_pokedex, name_pokedex, types, num_total, link]
        return_list.extend([attr.get_text() for attr in attrs])
        
        return return_list
