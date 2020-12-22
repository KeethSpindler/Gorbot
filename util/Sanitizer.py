class Sanitizer:
    
    def __init__(self, filth):
        self.filth = filth

class DrinkJsonSanitizer(Sanitizer):
    
    def __init__(self, json: dict):
        self.json = json
        Sanitizer.__init__(self, json)
    
    def clean_json(self):
        drink_dict = {}
        for key in self.json:
            if(self.json[key] != None):
                drink_dict[key] = self.json[key]  
        return drink_dict

    def __repr__(self):
        return f'DrinkJsonSanitizer Filth Type: {str(type(self.filth))}'