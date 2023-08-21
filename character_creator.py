#
# Solution for Pyflo Guided Project 3 - Character Creator
#

def print_head(hair, eye):
    '''
    This function is responsible for printing out the head of a custom character.
    The parameters:
      hair: Expected to be a 1-character string, used for the hair
      eye: Also expected to be a 1-character string, used for the eyes
    The function returns nothing.
    '''
    print(hair * 12)
    print(hair + '|        |' + hair)
    print(hair + '|  ' + eye + '  ' + eye + '  |' + hair)
    print(' |   /\   |' )
    print(' |        |' )
    print(' \  \'--\'  /')
    print('   ------')

def print_body(height, arm):
    '''
    This function is responsible for printing out the body of the custom character.
    The parameters:
      height: Expected to be an integer, used to determine the torso height
      arm: Expected to be a 1-character string, used for the arms
    The function returns nothing.
    '''
    print('     XX')
    print('#' + (arm*4) + 'XX' + (arm*4) + '#')
    print('    XXXX\n' * height, end='')

def print_legs(height, shoe):
    '''
    This function is responsible for printing out the legs of the custom character.
    The parameters:
      height: Expected to be an integer, used to determine the leg height
      shoe: Expected to be a 4-character string, representing the shoe
    The function returns nothing.
    '''
    print('    ====')
    print('   ||  ||\n' * height, end='')
    print(' ' + shoe + '  ' + reverse_shoe(shoe))

def reverse_shoe(shoe):
    '''
    This function reverses the show string.
    It can be used for general string-reversal as well.
    The parameter:
      shoe: Expected to be a 4-character string, representing the shoe
    The function returns the reversed shoe string.
    '''
    return shoe[::-1]

def main():
    print('Welcome to the custom character creator tool!')
    height = int(input('Overall character height: '))
    hair = input('Character for the hair: ')
    eye = input('Character for the eyes: ')
    arm = input('Character for the arms: ')
    shoe = input('4-character string for the shoes: ')
    segment = (height - 11) // 2

    print()
    print_head(hair, eye)
    print_body(segment, arm)
    print_legs(segment, shoe)

main()

