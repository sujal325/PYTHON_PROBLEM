def count(string):
    list_of_letters_in_string = list(string.lower())
    vowels = ["a", "e", "i", "o", "u"]
    count_number = 0
    for i in list_of_letters_in_string:
        if i in vowels:
            count_number += 1
    print(count_number)


count("This is Your FathEr")
