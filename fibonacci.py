def Fibonacci(Num):     
    if Num==0:
        print("Zero")
    elif Num==1:
        print("0")
    elif Num < 0:
        print("Invalidnumber",end=' ')
    else:
        fib1=0
        fib2=1
        fib3=0
        print(fib1,end='')
        print(fib2,end='')
        for i in range(2,Num):
            fib3=fib1+fib2
            print(fib3,end='')
            fib1=fib2
            fib2=fib3

Fibonacci(-21)