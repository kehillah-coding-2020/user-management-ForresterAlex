#Module Imports
import hashlib

#Function Imports
from register import register


#Main navigation prompt



exit = False

while not exit:

    print('1. Register')
    print('2. Other Stuff')
    print('3. Different Stuff')
    print('4. Exit')

    s = input('Make a selection: ')

    if s == '4':
        exit = True
    elif s == '1':
        print(register())
