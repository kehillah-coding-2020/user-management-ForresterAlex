#Module Imports
import hashlib

#Function Imports
from register import register
from login import login
from logout import logout
#Main navigation prompt


User = None
exit = False

while not exit:
    print("Current User: " + str(User))
    print('1. Register')
    print('2. Login')
    print('3. Logout')
    print('6. Exit')

    s = input('Make a selection: ')
    if s == '6':
        exit = True
    elif s == '1':
        User = register()
    elif s == '2':
        User = login()
    elif s == '3':
        User = logout()
