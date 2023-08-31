import string
import random
import math

'''Populate the characters to be used in a password'''
lowercase_list = list(string.ascii_lowercase)
uppercase_list = list(string.ascii_uppercase)
digits_list = list(string.digits)
punctuation_list = list(string.punctuation)

'''A while loop to ensure that an interger greater than 8 will be entered'''
while True:
    try:
        password_length = int(input('How long would you like the password to be? '))
        if password_length < 8:
            print('Password length should be more than 8 characters.')         
        else:  
            password_length = int(password_length)
            break
    except:
        print('Invalid character used!!!')


all_characters = lowercase_list + uppercase_list + digits_list + punctuation_list

'''break the characters into a 60% characters and 40% digits & punctuatons'''
a = password_length * (20/100)
b = password_length * (30/100)
x = math.floor(a)
y = math.floor(b)

'''Iterate character creation based on their ratio'''
password = []

for i in range(y):
    lowercase = random.choice(lowercase_list)
    password.append(lowercase)
    uppercase = random.choice(uppercase_list)
    password.append(uppercase)

for i in range(x):
    digits = random.choice(digits_list)
    password.append(digits)
    punctuation = random.choice(punctuation_list)
    password.append(punctuation)

'''To generate more characters to ensure the password length is achieved '''
z = (x * 2) + (y * 2)

if z != password_length:
    i = password_length - z

    for w in range(i):
        character = random.choice(all_characters)
        password.append(character)
else:
    pass

'''shuffle the password'''
random.shuffle(password)
password = "".join(password)


print(f"the password is {password}")
print(f"the lenth of the character is: {len(password)}")