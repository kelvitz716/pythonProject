restart = ('yes', 'Yes', 'YES', 'Y', 'y')

while True:  # Loop until user wants to stop
    user_choice = input("Do you want to continue? (yes/no): ")
    
    if user_choice not in restart:
        break  # Exit the loop if user doesn't want to continue
    
    phone_number = input("Enter your mobile number in the format: 'xxx-xxx-xxxxxx': ")
    
    if len(phone_number) != 14:
        print("The number should have exactly 14 characters")
    elif phone_number[3] != '-' or phone_number[7] != '-':
        print("Add '-' on the 4th and 8th characters")
    else:
        phone_number = phone_number.replace("-", "")
        if not phone_number.isdigit():
            print("The number has invalid characters")
        else:
            print("The number is correct!")
