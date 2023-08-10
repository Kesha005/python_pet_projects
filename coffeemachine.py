
class Coffe:
    
    def __init__(self, id, name, price):
        self.id = id
        self.name = name 
        self.price = price
    

class CoffeMachine:
    
    def __init__(self,coffee, user):
        self.coffee = coffee 
        self.user = user
    
    def show_menu(self):
      
        for data in self.coffee:
            print(f'{data.id}---{data.name}---{data.price}\n')
    
    
    def user_input_control(self, input_data):
        list_order = []
        for data in self.coffee:
            if data.id == int(input_data):
                list_order.append(data)
                
            else:
                pass
        if len(list_order) > 0:
            return self.cash_control(list_order[0])
        else:
            print("This coffee not in menu please select other one")
                
    
    def cash_control(self, coffee):
        if self.user.money >= coffee.price:
            self.user.money -= coffee.price
            print("Your coffee brewed sir")
        else:
            print("You dont have enough money for this coffee.Select another one")
    
    
class User:
    def __init__(self, money):
        self.money = money
        


coffees = [
    Coffe(1, "Capuchino", 0),
    Coffe(2, "Americano", 10),
    Coffe(3, "Espresso", 20)
]


person = User(int(input("How much money do you have: ")))

coffee_machine = CoffeMachine(coffees, person)


select_coffee = ''
while select_coffee != 'exit':
    
    coffee_machine.show_menu()
    select_coffee = (input("Which coffe do you want brew: "))
    
    if select_coffee == 'exit':
        exit()
    else:
        coffee_machine.user_input_control(select_coffee)
     
    
    
    
    
