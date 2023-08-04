from collections import defaultdict



text = ["Bu gun yurdumyzda bayramcylyk gecirildi.Su bayramcylykda her bir gelen myhmana kitap paylanyldy.Berlen kitap dasary yurt yazyjylarynyn kitaplarydy.Ol kitaplary myhmanlar gowy gordi"]

temp = defaultdict(int)

for sub in text:
    for word in sub.split():
        temp[word] += 1
        
response = max(temp, key=temp.get)



print(f'Word with maximum frequensy is: {response}')