#calculate margin
earned = int(input('How much money did you earn? '))
spent = int(input('How much money did you spend? '))
if earned > spent:
    print('Great! you earned more than you spent. Good job.')
if earned == spent:
    print('Wow, you broke even.')
if earned < spent:
    print('You are in a deficit of -' + str(spent-earned))
print("\n")

#check passport
current_year = int(input('what year is it? '))
received_year = int(input('What year did you get your passport? '))
if received_year + 10 < current_year:
    print('You should go get a new passport!')
elif received_year + 10 == current_year:
    print('You should get a new passport sometime soon')
else:
    print('You do not need to get a new passport for now')
print('\n')

#check height
height = int(input('Enter your height '))
if height > 20 and height < 70:
    print('You may pass')
else:
    print('Entry rejected')
print('\n')

#spanish class
spanish_level = input('What is your Spanish knowledge? ')
if spanish_level == 'none':
    print('You should take Spanish 101')
elif spanish_level == '101':
    print('You should take Spanish 102')
elif spanish_level == '102':
    print('You should take Spanish 201')
elif spanish_level == '201':
    print('You should take Spanish 202')
elif spanish_level == '202':
    print('You should take Advance Spanish')
else :
    print("Sorry, I didn't recognize what you entered.")
    print("Please give me one of these experience levels: none, 101, 102, 201, or 202.")
print('\n')
