'''
Contributed by @Hinal-Srivastava

While loop is used to iterate over a block of code repeatedly until a given condition returns false.
Syntax:
while condition:
    #body_of_while

'''

#Case - 1
num = 1
while num < 10:
    print(num)
    num+= 3
print('\n')    

#Case - 2: Infinite While Loop
'''
Infinite because here there is no increament statement for num and the given condition will remain true always
'''
num = 1
while num<5:
   print(num)
print('\n')   

#Case - 3: Nested Loop
i=1
while i<=3 :
    print(i,"Outer loop is executed only once")
    j=1
    while j<=3:
        print(j,"Inner loop is executed until to completion")
        j+=1
    i+=1
print('\n')

#Case - 4: While-else Loop 
num = 1
while num < 3:
    print("Inside loop")
    num+= 1
else:
    print("Inside else")
