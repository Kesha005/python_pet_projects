from bs4 import BeautifulSoup
import json
import requests
from collections import namedtuple

URL = 'https://turkmenportal.com/blog/novosti/'
# grid_block
# items
# entry style-media borderless media type-post


posts = [] 

response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")


grid_block = soup.find("div", {"class":"grid_block"})

# print(grid_block.encode('utf-8'))

items = grid_block.find("div",{"class":"items"})

articles = items.find_all("article",{"class":"entry style-media borderless media type-post"})


for post in articles:
    
    class_a = post.find('div', {"class":'entry-title'})
    name = class_a.find("a").text
    url = class_a.find("a").get("href")
    short_title = post.find('div',{'class':'post-content'}).text
    posts.append({"name":name, "short_title":short_title, "url":url})
   
    
with open("turkmenportal.json", "w") as file :
    json.dump(posts, file, indent=4)
    
