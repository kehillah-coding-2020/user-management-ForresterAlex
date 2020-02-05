#Register Fucntion to recorod data from users, and write to database

#Modue Imports
import getpass
#File Imports

#Register Function
def register():
    '''
    Registers a user to the database
    '''
    exit = False
    while not exit:
        uname = input("Input a username (15 char max): ")
        if len(uname) <= 15:
            exit = True
        else:
            print("Username too long, 15 char limit")
            exit = False
    print(uname)
    exit = False
    while not exit:
        pass1 = getpass.getpass('Input Password: ')
        print("*" * len(pass1))
        pass2 = getpass.getpass("Verify Password: ")
        if not pass1 == pass2:
            print("Bad password match")
        else:
            with open('UserDatabase.txt','a') as pass_database:
                pass_database.write(uname + '\t' + pass1 + '\n')
            exit = True
    return uname
