def largest(list):
    n = list[0]
    for i in list:
        if i >= n:
            n = i
    print(n)


list = [1, 2, 3, 5, 2, 3, 6, 7, 8, 9, 1, 1, 1]
largest(list)
