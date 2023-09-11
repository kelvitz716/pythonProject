import datetime as dt
import time as tm


file = 'todo.txt' #input('Enter the file name: ')

def add_task(due_year, due_month, due_day, new_line):
    todo_file = open(file, 'a')
    that_day = dt.datetime(due_year,due_month,due_day)
    print(f"j: {that_day}")
    todo_file.write(f'{that_day}     ' )
    todo_file.write(new_line + '\n')
    todo_file.close()

def show_tasks():
    todo_file = open(file, 'r')
    numbering = 1
    content = todo_file.readlines()
    today = dt.date.today()

    for line in content:
        due_year = int(line[:4])
        due_month = int(line[5:7])
        due_day = int(line[8:10])
        that_day = dt.date(due_year,due_month,due_day)
        remaining_time = that_day - today
        remaining_day = remaining_time.days      
        if that_day != today:
            print(f"({numbering}) due in {remaining_day} is {line}")
        else:    
            print(f"({numbering}) Today is due date for {line}")        

        
        numbering += 1
    if numbering == 1:
        print("The list is empty.")

    todo_file.close()   

  

def delete_task(numbering):
    todo_file = open(file, 'r')
    d = todo_file.readlines()
    new_content = ''
    counter = 1 
    todo_file.seek(0)
    for i in d:
        if counter != int(numbering):
            new_content += i
        if counter == int(numbering):
            print(f'deleted task is: {i}')
        counter += 1
    todo_file.close()
    todo_file = open(file, 'w')
    todo_file.write(new_content)
    todo_file.close()


def calculating_due_date():
    todo_file = open(file, 'r+')
    numbering = 1
    for i in todo_file,:
        print(f"{numbering}.  {i}S")
        numbering += 1
    todo_file.close()

    todo_file = open(file, 'r')
    d = todo_file.readlines()
    counter = 1 
    today = dt.date.today()
    
    for i in d:
        due_year = int(i[:4])
        due_month = int(i[5:7])
        due_day = int(i[8:10])
        that_day = dt.date(due_year,due_month,due_day)
        remaining_time = that_day - today
        remaining_day = remaining_time.days()
    
        if that_day != today:
            print(f"{numbering}. due in {remaining_day} is {i}")
            print( end='')
        else:            
            print("Today is due date:") 
        counter += 1 
    print('\v')
    todo_file.close()
    


def main():
    command = ''
    while command != 'exit':
            #print('\n')
            command = input('Do you want to add, delete, due, show or exit the To-Do list? '.strip())
            if command == 'add'.lower():
                new_line = input('Enter your new task: ')
                some_year = int(input('Enter the due date Year: '))
                some_month = int(input('Enter the due date Month: '))
                some_day = int(input('Enter the due date Day: '))
                add_task(some_year, some_month, some_day, new_line)
            elif command == 'delete':
                numbering = input('which task number is completed? ')
                delete_task(numbering)
            elif command == 'show':
                show_tasks()
            elif command == 'due':
                calculating_due_date()
    print('Goodbye!!')
main()
