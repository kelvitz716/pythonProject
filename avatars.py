#head
def print_head(hair, eye):
    print(hair * 12)
    print(hair + '|        |' + hair)
    print(hair + '|  ' + eye + '  ' + eye + '  |' + hair)
    print(' |   /\   |' )
    print(' |        |' )
    print(' \  \'--\'  /')
    print('   ------')


#body
def print_body(height, arm):
    print('     XX')
    print('#' + (arm*4) + 'XX' + (arm*4) + '#')
    print('    XXXX\n' * height, end='')
    
#Shoe String Reversal
def reverse_shoe(shoe_string):
    reversed_shoe = shoe_string[::-1]
    return reversed_shoe

#legs
def print_legs(height, shoe_string):
    print ('    ==== ')
    print('   ||  ||\n' * height, end='')
    print(shoe_string + '  ' + reverse_shoe(shoe_string))

#main
def main():
    print('Welcome to the custom character creator tool!')
    height = int(input('Overall character height: '))
    hair = input('Character for the hair: ')
    eye = input('Character for the eyes: ')
    arm = input('Character for the arms: ')
    shoe_string = input('4-character string for the shoes: ')
    segment = (height - 11) // 2

    print()
    print_head(hair, eye)
    print_body(segment, arm)
    print_legs(segment, shoe_string)

main()
