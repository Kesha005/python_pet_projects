class User:
    
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
    
    def minus_user_money(self, value):
        self.money = self.money - value
    
    
    
user = User("Kerim", 12, 4500)
print(user.money)
user.minus_user_money(34)
print(user.money)
        