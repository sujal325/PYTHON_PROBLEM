def palindrome(string):
    t = len(string)
    forward = 0
    backward = -1
    n = 1
    while n <= (t / 2):
        if string[forward] != string[backward]:
            print("This is not palindrome.")
            return
        forward += 1
        backward -= 1
        n += 1
    print("This is palindrome.")


stri = input("Give string: ")
palindrome(stri)
