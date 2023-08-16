title = "Welcome to Python"
print(title)
title.capitalize

#calculate years
import time

current_year = int(time.strftime('%Y'))
birth_year = int(input("what is your birth year?"))
age = current_year - birth_year
print("your are " + str(age) + " years old")

print("the", end=' ')
print('big', end=' ')
print("black", end=' ')
print('box', end=' ')
print("\n")

#print number to 100
i = int(input('Select your number'))

while i<=100:
    print(i)
    i = i+5

print("this is greater than 100")

    

