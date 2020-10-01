#american phone number
#

def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone number-sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False #no area code
    if text[3] != '-':
        return False #missing dash

    for i in range(4,7):
        if not text[i].isdecimal():
            return False #no first 3 digits
    if text[3] != '-':
        return False #missing dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False #last 4 digits

    return True
#print(isPhoneNumber('415-555-1234'))
#print(isPhoneNumber('hello'))

message= 'Call me 415-555-1234 tommorrow or at 415-555-9999'

foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone nmuber found: '+ chunk)

if not foundNumber:
        print('Could not find any number')
        
