import re

message= 'Call me 415-555-1234 tommorrow or at 415-555-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group()) #tells the actual text

print(phoneNumRegex.findall(message))
