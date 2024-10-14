def fibo(value):
    num1 = 0
    num2 = 1
    nextnum = 0
    n = 1
    while n <= (value - 2):
        nextnum = num1 + num2
        num1 = num2
        num2 = nextnum
        n += 1
    print(num2)


fibo(18)
