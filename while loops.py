#count from 1 to 10
i = 1
while i <= 4:
    print(str(i))
    i = i + 1
print('the end')
print('\n')

#A program to sum up all of the numbers between 1 and 1000 and print out the result.
i = 1
sum = 0
while i <=10:
    sum += i
    i += 1  
print('the sum is ' + str(sum) + '\n')

#A program to print out pyramid-shaped text.
i = 1
pyramid = int(input('Enter the pyramid width '))
while i <= pyramid:
    spacing = pyramid - i
    print(' ' * spacing + '#' * (i*2))
    i += 1
print('the end')
print('\n')

#
sentence = 'There once lived a bee in a house by the sea.'

position = 0
while position < len(sentence)-10:
    
    index = position
    while index < 10:
        print(sentence[index], end='')
        index += 1

    print('\n')
    position += 1
print('\n')

#counts of upper and lower case letters
text = input('Type some text and then press ENTER: ')
uppercase_count = 0
lowercase_count = 0
for index in range(0, len(text)):
    char = text[index]
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
print("Number of upper-case letters:", uppercase_count)
print("Number of lower-case letters:", lowercase_count)
print('\n')

#Divisible by 
start = int(input('What value should we start at? '))
end = int(input('What value should we end at? '))
divide = int(input('What number to check divisibility for? '))
number = start
while number < end:
    if number % divide == 0:
        print(number, 'is divisible by', divide)
    number += 1