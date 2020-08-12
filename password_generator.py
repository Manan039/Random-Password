import string
import random

stock=list(string.ascii_letters + string.digits + string.punctuation)
password=''

n = int(input('Enter the no. of digit required in the password -> '))

for i in range (0,n):

    password+=random.choice(stock)

print(f'The generated password is--> {password}')
    
    
