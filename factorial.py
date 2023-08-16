number = int(input('Enter your number '))
factorial = 1
if number == 0:
    print('The factorial is 1')
elif number < 0:
    print('The number has to be a positive number')
else:
    for i in range(1,number + 1):
        factorial = factorial*i
    print("The factorial of " + str(number) + " is " + str(factorial))
print('\n')