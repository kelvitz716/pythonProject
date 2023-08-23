def lookup_employee(employees):
    name = input('Employee name: ')
    for employee in name:
        if 'name' in employee and employee['name'] == name:
            print('Information for ' + name + ':')
            for key, value in employee:
                print('  ' + str(key) + ' -> ' + str(value))
            return
    print('Employee not found')