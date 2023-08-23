from bs4 import BeautifulSoup
from pprint import pprint
import json
import requests

urls = []

post_body = []

with open('islenen.json','r') as file:
    data = json.load(file)


for url in data:
    urls.append(url)
print('Urls is imported')
    

for i in range(1,len(urls)):
    try:
        response = requests.get(urls[i]['url'])
        soup = BeautifulSoup(response.content,'html.parser')
        content = soup.find('div',{'class':'content'})
        page_header = content.find('div',{'class':'page-header'})
        name  = page_header.find('h3').text
        post_content = content.find('div',{'class':'post-body'})
        body = post_content.find('p').text
        post_body.append({'name':name,'body':body})
        print(f'{i} post success')
    except:
        continue
    
with open('islenen_body.json','w') as write_file:
    json.dump(post_body, write_file)