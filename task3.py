## PASSWORD GENERATOR ##

import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','#','$','%','&','*']
print('-- welcome to PASSWORD GENERATOR --')

n_letters =int(input("enter how many letters you want in your password?\n"))
n_num =int(input("enter how many numbers you want in your password?\n"))
n_symbol =int(input("enter how many symbol you want in your password?\n"))

password = ""

for i in range (1,n_letters+1):
    n = random.choice(letters)
    password = password + n
# print(password)    
for i in range (1,n_num+1):
    n = random.choice(num)
    password = password + n
# print(password) 
for i in range (1,n_symbol+1):
    n = random.choice(symbol)
    password = password + n

print(password) 

