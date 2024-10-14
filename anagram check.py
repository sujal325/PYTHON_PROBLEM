def anagram(val1, val2):
    length1 = len(val1)
    length2 = len(val2)
    if length1 != length2:
        print("It is not anagram.")
        return
    value1 = list(val1.lower())
    value2 = list(val2.lower())
    for i in value1:
        if i not in value2:
            print("It is not anagram.")
            return
    for i in value2:
        if i not in value1:
            print("It is not anagram.")
            return
    print("It is anagram")


anagram("flus ter", "restf ul")
