class Formatter():
    
    def __init__(self, arg):
        self.arg = arg

    def get_filth_type(self):
        return f'Type: {str(type(self.arg))}'

class DrinkFormatter(Formatter):
    
    def __init__(self, json: dict):
        if(isinstance(json, dict) != True):
            raise TypeError('The argument must be of type dict')
        self.json = json
        Formatter.__init__(self, json)

    def make_ingredients_string(self):
        ingredients = [self.json.get(ing) for ing in self.json if 'Ingredient' in ing and self.json.get(ing) is not None]
        measurements = [self.json.get(measure) for measure in self.json if 'Measure' in measure and self.json.get(measure) is not None]
        if(len(measurements) == 0):
            return ingredients
        ingredient_list = []
        for i in range(len(ingredients)):
            if(i < len(measurements)):
                ingredient_list.append(measurements[i].strip() + " " + ingredients[i])
            elif(ingredients[i] == ' '):
                pass
            else:
                ingredient_list.append(ingredients[i])
        return ingredient_list

    def __repr__(self):
        return f'DrinkFormatter Arg Type: {str(type(self.json))}'