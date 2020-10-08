#identify strong password
import re
pwd = input('Enter a Password :')
if (len(pwd) < 8 ):
    print("Weak Password and less then 8 characters")
else:
    num = re.findall('[0-9]',pwd)
    upe = re.findall('[A-Z]',pwd)
    low = re.findall('[a-z]',pwd)
    spe = re.findall('[~!@#$%^&*_-]',pwd)    #special characters
    if (len(num) >= 1 and len(upe) >= 1 and len(low) >= 1 and len(spe) >= 1):
        print("Strong Password")
    elif (len(upe) < 1):
        print("Missing Upper-case character")
    elif (len(low) < 1):
        print("Missing Lower-case character")
    elif (len(num) < 1):
        print("Missing Numerical character")
    elif (len(spe) < 1):
        print("Missing Special character")
        
