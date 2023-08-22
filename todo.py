#
# Solution for Pyflo Guided Project 4 - The To-Do List
#

# This is a global constant that stores the name of the file to save the todo list content into.
FILE_NAME = 'todo.txt'

def show_todo_list():
    '''
    This function should display all of the elements in the todo list file formatted
    as a numbered list of elements and each line should start with an asterisk..
    There are no parameters or return values.
    '''
    todo_file = open(FILE_NAME, 'r')
    counter = 1
    for line in todo_file:
        line = line.strip('\n')
        print('  * (' + str(counter) + ') ' + line)
        counter += 1
    if counter == 1:
        print("Nothing in the list!")
    todo_file.close()

def add_to_todo_list(item):
    '''
    This file adds a new item to the todo list. It does so by opening up the todo list file,
    appending exactly one line with the new element, and then closes the file.
    The parameter:
      item: a string representing the item to add to the list.
    This function returns nothing.
    '''
    todo_file = open(FILE_NAME, 'a')
    todo_file.write(item + '\n')
    todo_file.close()

def remove_from_todo_list(number):
    '''
    This function removes one item from the todo list. It accomplishes this by opening the todo
    list file, loading all of the content except for the line to remove into a string, and then
    over-writing the old todo list file with the new content.
    The parameter:
      number: An integer representing the list number of the item to remove.
    This function returns nothing.
    '''
    todo_file = open(FILE_NAME, 'r')
    new_content = ''
    counter = 1
    for line in todo_file:
        if counter != number:
            new_content += line
        counter += 1
    todo_file.close()
    todo_file = open(FILE_NAME, 'w')
    todo_file.write(new_content)
    todo_file.close()

def main():
    '''
    This is the main function!
    It handles the command loop logic, and calls the other functions when necessary.
    '''
    command = ''
    while command != 'exit':
        command = input('show, add, remove, or exit? ')
        if command == 'show':
            show_todo_list()
        elif command == 'add':
            task = input('What task needs to be added? ')
            add_to_todo_list(task)
        elif command == 'remove':
            number = int(input('What item number should be removed? '))
            remove_from_todo_list(number)
    print('Goodbye!')

main()

