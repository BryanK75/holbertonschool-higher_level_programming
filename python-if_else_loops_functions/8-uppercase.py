#!/usr/bin/python3
def uppercase(str):
    if str == "":
        print("Empty string")
        return
    for c in str:
        print("{}".format(chr(ord(c) - 32) if 'a' <= c <= 'z' else c), end="")
    print()
