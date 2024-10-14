import math


def armstrong(value):
    ctl = list(value)
    target = int(value)
    cv = 0
    nv = 0
    for i in ctl:
        cv = int(i)
        nv += math.pow(cv, 3)
    if nv == target:
        print("It is a armstrong number.")


value = input("Give number: ")
armstrong(value)
