import json 
from collections import namedtuple



Coffe = namedtuple('Coffe', [
    'name', 'price'
])


coffees = []

with open ("coffe.json", "r") as file:
    result = json.load(file)
    for data in result:
        coffees.append(Coffe(data["name"], data["price"]))
    
for coffee in coffees:
    print(f'Name: {coffee.name}\t Price: {coffee.price}\n' )
    print("--------------------------------")
    
    

