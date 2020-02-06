#Module Imports
import getpass
#Function Imports
def delete(User):
    Exit = False
    while not Exit:
        if User == None:
            print("There is no user logged in")
            Exit = True
        else:
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
