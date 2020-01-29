#Login function to compare user data to database and authenticate

#Module Imports
import getpass

#File Imports

def login():
    '''
    Prompt user for login info
    '''
    exit = False
    while not exit:
        uname = ''
        passcode = ''
        uname = input("Enter your username: ")
        passcode = getpass.getpass("Enter your password: ")
        UData = open("UserDatabase.txt", 'r')
        for line in UData:
            user_data = line.split('\t')
            user_data[1] = user_data[1].strip()
            if user_data[0] == uname:
                if user_data[1] == passcode:
                    exit = True
        if exit == False:
            print("Please enter a valid username and passcode")
        UData.close()
        User = uname
    return "Authentication Success"
