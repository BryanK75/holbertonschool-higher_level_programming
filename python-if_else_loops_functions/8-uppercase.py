#!/usr/bin/python3
def uppercase(str):
    for c in str:
        # if c is lowercase, convert to uppercase; else leave as is
        print("{}".format(chr(ord(c) - 32) if 'a' <= c <= 'z' else c), end="")
    print()  # new line at the end
