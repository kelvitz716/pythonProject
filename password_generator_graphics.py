from tkinter import *
import string
import random
import math


def generate_password(password_length):
    lowercase_list = list(string.ascii_lowercase)
    uppercase_list = list(string.ascii_uppercase)
    digits_list = list(string.digits)
    punctuation_list = list(string.punctuation)

    all_characters = lowercase_list + uppercase_list + digits_list + punctuation_list
    
    '''break the characters into a 60% characters and 40% digits & punctuations'''
    a = password_length * (20/100)
    b = password_length * (30/100)
    x = math.floor(a)
    y = math.floor(b)

    '''Iterate character creation based on their ratio'''
    password = []

    for _ in range(y):
        lowercase = random.choice(lowercase_list)
        password.append(lowercase)
        uppercase = random.choice(uppercase_list)
        password.append(uppercase)

    for _ in range(x):
        digits = random.choice(digits_list)
        password.append(digits)
        punctuation = random.choice(punctuation_list)
        password.append(punctuation)

    '''To generate more characters to ensure the password length is achieved '''
    z = (x * 2) + (y * 2)

    if z != password_length:
        i = password_length - z

        for _ in range(i):
            character = random.choice(all_characters)
            password.append(character)
    else:
        pass
    
    return password

def generate_password_and_display():
    password_length = int(length_entry.get())
    generated_password = generate_password(password_length)
    generated_password = "".join(generated_password)
    password_display.config(text=generated_password)


window = Tk()
window.geometry("600x600")
window.title("Random Password Generator")

length_label = Label(window, text="Enter password length:")
length_label.pack(pady=10)

length_entry = Entry(window)
length_entry.pack()

generate_button = Button(window, text="Generate password", command=generate_password_and_display)
generate_button.pack()

password_display = Label(window, text="", wraplength=300)
password_display.pack()

window.mainloop()






