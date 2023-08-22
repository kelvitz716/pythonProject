#show list
def show_todo_list():
    # Put your code here!
    f = open('todo.txt', 'r')
    count = 1
    for line in f:
        print('*  (' + str(count) + ') ' + line)
        count += 1
    f.close()
#add list
def add_to_todo_list(item):
    # Put your code here!
    f = open('todo.txt', 'a')
    f.write(item + '\n')
    f.close()

#remove list
def remove_from_todo_list(number):
    # Put your code here!
    f = open('todo.txt', 'r+')
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i != number:
            f.write(i)
    f.truncate()

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
