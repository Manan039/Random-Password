import random
n=int(input("Enter password length"))
s="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$&"
x=''.join(random.choices(s,k=n))
print(x)
