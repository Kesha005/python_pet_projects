import requests


URL = 'http://turkmenportal.com'


response = requests.get(URL)

print(response.content)


