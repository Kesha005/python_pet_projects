from bs4 import BeautifulSoup
import json
import requests
from pprint import pprint

URL = 'https://biz.islenen.ru/bilim/'

URL_SCRAP = 'https://biz.islenen.ru/bilim/page/'

posts = []

response  = requests.get(URL)

soup = BeautifulSoup(response.content,'html.parser')

all_body = soup.find('body')

ul = all_body.find('ul',{"class":'pagination'})

li = ul.find('li',{'class':'active'})

hrefs = []

page_count=[]

a_block = li.find_all('a')

for href in a_block:
    page_count.append(int(href.text))


for i in range(2,page_count[-1]+1):
    get_posts = requests.get(URL_SCRAP+str(i))
    souping = BeautifulSoup(get_posts.content,'html.parser')
    body = souping.find('body')
    contents = all_body.find_all('div',{'class':'content'})
    for post in contents:
        a_block = post.find('h4')
        post_name = a_block.find('a').text
        url = a_block.find('a').get('href')
        posts.append({"name":post_name,"url":url})
    print(f'{i} page accepted')
    
with open("islenen.json","w") as file:
    json.dump(posts, file,indent=4)