import random
n = 20
guessed = int(n * random.random()) + 1
guess = 0
while guess != guessed:
    guess = int(input("New number: "))
    if guess > guessed:
        print("Number is larger.")
    elif guess < guessed:
        print("Number is lesser.")
else:
    print("Congratulation! You guessed right!!")