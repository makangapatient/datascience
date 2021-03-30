import datetime

name = input('Please enter your name. \n') #ask user for their name
allowedUsers = ['Patient', 'Doxa'] #allowed user 
allowedpass = ['Patient@23456', 'Doxa@pass234'] #allowed user's password
now = datetime.datetime.now()
balance = 0

if(name in allowedUsers):
    upass = input('Please enter the password. \n') #ask user to enter the password
    userId = allowedUsers.index(name)
    
    #check if the user password is allowed
    if(upass == allowedpass[userId]):
        print('Welcome %s' %name) #welcome the user
        print()
        
        #Displaying date time
        print('Current date and time: ') 
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print()
        
        #Select ATM options
        print('These are the available options: ')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('2. Complaint')
        print()
        
        #Invite user to select an option
        selectedOption = int(input('Please select an option: '))
        
        if(selectedOption == 1):
            print('How much would you like to withdraw? \n')
            userWithdra = int(input('Enter the Amounths: \n')) #invite the user to input the amounths
            print()

            print('Take your cash') #invite the user to take the cash
            
        elif(selectedOption == 2):
            print('How much would you like to deposit? \n')
            userDeposit = int(input('Please enter the amounth: \n'))
            
            balances = balance + userDeposit #calculate the current balance
            print('Current balance is : ', balances)
            print()
            
        elif(selectedOption == 3):
            print('What issue will you like to report? \n')
            report = input('Please enter the issue: \n')
            print('Thank you for contacting us')
            
        else:
            print('Invalid option selected, please try again')
    else:
        print('Password incorect, please try again')
else:
    print('Name not found, please try again')
