def fun(variable):
	letters=['a','e','o','i','u']
	if (variable in letters):
		return True
	else:
		return False

sequence=['g','e','w','a','k','s','p','r']
filtered=filter(fun,variable)
print("The filtered letters are:")
for s in filtered:
	print(s)