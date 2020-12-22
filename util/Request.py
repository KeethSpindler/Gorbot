class Request:
    def __init__(self, requests):
        self.requests = requests
        self.urls = {
            "cocktail_db_api": 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
        }
    
    def get_drink_json(self):
        return self.requests.get(self.urls['cocktail_db_api']).json()['drinks'][0]   