#Login function to compare user data to database and authenticate

#Module Imports
import getpass

#File Imports
UData = open("UserDatabase.txt", 'r')

def login():
    '''
    Prompt user for login info
    '''
    exit = False
    while not exit:
        uname = input("Enter your username: ")
        passcode = getpass.getpass("Enter your password: ")
        for line in UData:
            user_data = line.split('\t')
            passcode = passcode + '\n'
            if user_data[0] == uname:
                if user_data[1] == passcode:
                    exit = True
                else:
                    print("Please enter a valid username and passcode")
            else:
                print("Please enter a valid username and passcode")
    print("Authentication Success")
