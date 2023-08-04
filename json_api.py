import json 
import requests
from pprint import pprint
from collections import namedtuple


URL = 'https://api.github.com/users?since=Kesha'


GithubUsers = namedtuple('GithubUsers', [
    'username', 'user_url'
])

class GetterFromApi:
    
    def __init__(self, url):
        self.url = url
    
    
    def get_data_from_url(self):
        result = requests.get(self.url).json()
        return result
    
    def get_and_convert_to_json(self, file_name):
        data = self.get_data_from_url()
        
        filepath = file_name + ".json"
        
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
        
    
file_name = input("Enter the filename: ")

github_users = GetterFromApi(URL)

github_users.get_and_convert_to_json(file_name)

