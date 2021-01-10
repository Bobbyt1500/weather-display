import requests

class OMWAPI():
    def __init__(self, api_key):
        self.apikey = api_key
    
    def make_request(self, url):
        response = requests.get(url+"&appid="+self.apikey)
        return response.json()
