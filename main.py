#Module Imports
import hashlib

#Function Imports
from register import register
from login import login

#Main navigation prompt



exit = False

while not exit:

    print('1. Register')
    print('2. Login')
    print('3. Different Stuff')
    print('4. Exit')

    s = input('Make a selection: ')

    if s == '4':
        exit = True
    elif s == '1':
        print(register())
    elif s == '2':
        User = login()
