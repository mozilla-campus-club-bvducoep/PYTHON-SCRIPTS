x = input('Enter value of x: ')  
y = input('Enter value of y: ')  
  
# create a temporary variable and swap the values  
temp = x  
x = y  
y = temp  
  
print('The value of x after swapping: {}'.format(x))  
print('The value of y after swapping: {}'.format(y))  

"""
The above code uses temporary variable for the calculations.
	Without using third variable: x,y=y,x
	or
	x=x+y
	y=x-y
	x=x-y
	For better understanding take an example of x=10,y=20.
"""