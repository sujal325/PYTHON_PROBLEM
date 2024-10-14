def reverse(string):
    string = list(string)
    empty_string = []
    length_in_negative = (1 - len(string)) - 2
    for i in range(-1, length_in_negative, -1):
        empty_string.append(string[i])

    reversed_string = "".join(empty_string)
    print(reversed_string)


reverse("sujal")
