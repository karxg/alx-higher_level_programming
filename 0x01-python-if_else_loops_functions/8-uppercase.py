#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{:c}".format(65 + (ord(char) - 97)
                            if ord(char) >= 97 and ord(char) <= 122
                            else ord(char)), end="")
    print("")
