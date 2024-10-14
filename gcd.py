def gcd(val1, val2):
    while val2 != 0:
        val1, val2 = val2, val1 % val2
    print(val1)


gcd(3, 123)
