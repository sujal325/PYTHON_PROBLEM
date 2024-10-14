import math


def prime(value):
    for i in range(2, math.isqrt(value)):
        if value % i == 0:
            print("It is not prime number.")
            return
    print("It is a prime number.")


prime(21)
