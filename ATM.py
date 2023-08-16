print("Welcome to the ATM")
balance = 1000
chances = 3
restart = ('Yes','yes','YES','Y','y')
#pin check
while chances >= 0:
    pin = int(input("Enter your pin number: "))
    if pin != 0000:
        print("Incorrect pin: Try again!!")
        chances = chances - 1
        if chances == 0:
            print("Account locked.")
            break
    else:
        #options
        while restart not in ('no','No','NO','N','n'):
            option = int(input('''Welcome to your account \n
            Select 1 to check your balance:\n    
            Select 2 to make withdrawal:\n
            Select 3 to pay in:\n
            Select 4 to return card:\n'''))
            #first option
            if  option == 1:
                print("Your account balance is  " + str(balance))
                restart = input("Would you like to restar; ")
                if restart in ('no','No','NO','N','n'):
                    print("Thank you")
                    break
             #second option   
            elif option == 2:
                withdrawal = int(input("How much would you like to withdraw? "))
                if withdrawal > balance:
                    print("You have insufficient funds")
                else:
                    balance = balance - withdrawal
                print("Your balance is " + str(balance))
                restart = input("Would you like to restar; ")
                if restart in ('no','No','NO','N','n'):
                    print("Thank you")
                    break
            #third option    
            elif option == 3:
                deposit = int(input("How much would you like to deposit: "))
                balance = balance + deposit
                print("Your new balance is " + str(balance))
                restart = input("Would you like to restar; ")
                if restart in ('no','No','NO','N','n'):
                    print("Thank you")
                    break
            #fourth option    
            elif option ==4:
                print("Drop your card at the nearest bank offices")
            else:
                print("Invalid option.")
                restart = input("Would you like to restar; ")
                if restart in ('no','No','NO','N','n'):
                    print("Thank you")
                    break
