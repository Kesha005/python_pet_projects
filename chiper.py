

dictionary ={
    'q':'~','w':'@','e':'#','r':'$','t':'%','y':'^','u':'&','i':'*',
    'o':'(', 'p':')','a':'-','s':'_','d':'=','f':'+','g':'<','h':'>',
    'j':'/','k':'?','l':'.','z':',','x':'`','c':'4','v':'5','b':'0','n':'8','m':'!',
    '1':'a','2':'f','3':'g','4':'k','5':'m','6':'n','7':'v','8':'x','9':'d','0':'x',
}


user_input = input("Enter the some words: ").lower()


chiping = list(user_input)




for char in range(len(chiping)):
    if chiping[char]!=' ':
        chiping[char] = dictionary[chiping[char]]
    pass
    
    

coded = ''.join(chiping)


print(coded)