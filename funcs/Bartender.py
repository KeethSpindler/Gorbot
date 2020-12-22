class Drink():

    def __init__(self, json, sanitizer, formatter, embedder):
        
        self.sanitizer = sanitizer(json)
        json = self.sanitizer.clean_json()
        self.formatter = formatter(json)
        self.img = json.get('strDrinkThumb')
        self.name = json.get('strDrink')
        self.category = json.get('strCategory')
        self.alcoholic = json.get('strAlcoholic')
        self.glass = json.get('strGlass')
        self.ingredients = self.formatter.make_ingredients_string()
        self.instructions = json.get('strInstructions')
        self.embed = embedder(self).embed
        
    def __repr__(self):
        new_line='\n'
        tab = '\t'
        bracket = '{}'
        rerp_string = f'Drink{bracket[0]}{new_line}{tab}name: {self.name},{new_line}{tab}category: {self.category},{new_line}{tab}alcoholic: {self.alcoholic},'
        rerp_string += f'{new_line}{tab}glass: {self.glass},{new_line}{tab}ingredients: {self.ingredients},{new_line}{tab}instructions: {self.instructions},'
        rerp_string += f'{new_line}{tab}image: {self.img},{new_line}{tab}embed: {self.embed},{new_line}{tab}{new_line}{tab}sanitzier: {self.sanitizer},'
        rerp_string += f'{new_line}{tab}{new_line}{tab}formatter: {self.formatter},{new_line}{tab}{bracket[1]}'  
        return rerp_string 