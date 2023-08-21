day = input('What is the date today? ')
file_name = day + '.txt'
sales = open(file_name, 'w')

count = int(input('How many products were sold today? '))
while count > 0:
    product = input('Product name: ')
    quantity = input('Product sales quantity for the day: ')
    sales.write(product + ',' + quantity + '\n')
    count -= 1

sales.close()
