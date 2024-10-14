def factorial(value):
    n = value
    new_value = 1

    while n >= 1:
        new_value *= value
        value -= 1
        n -= 1
    print(new_value)


factorial(5)
