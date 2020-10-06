num = int(input(""))
temp = num
rev = 0
while temp != 0:
    rev = (rev * 10) + (temp % 10)
    temp = temp // 10
if num == rev:
	print("The number {} is palindrome".format(num))
else:
    print("The number is not palindrome".format(num))