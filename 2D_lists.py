grid = [ [1, 2], [3, 4] ]
x = grid[1][0]
y = grid[0][1]
print(x+y)
print('\n')

def add_food(pantry):
    '''
    This function should add a new food 
    item to the pantry dictionary.
    '''
    food_name = input('Enter the food name: ')
    calories = int(input('Enter the food calories: '))
    pantry[food_name] = calories

def remove_food(pantry):
    '''
    This function should remove an existing 
    food item from the pantry dictionary.
    '''
    food_name = input('food to remove: ')
    if food_name in pantry:
        del pantry[food_name]

def show_food(pantry):
    '''
    This function should show all foods
    that exist in the pantry.
    '''
    for key in pantry:
        print(key, '-->', pantry[key])

def main():
    pantry_items = {}
    command = ''
    while command != 'done':
        command = input('Type add, remove, show, or done: ')
        if command == 'add':
            add_food(pantry_items)
        elif command == 'remove':
            remove_food(pantry_items)
        elif command == 'show':
            show_food(pantry_items)
main()