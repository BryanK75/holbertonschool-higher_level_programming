#!/usr/bin/python3
"""
    File function for read_file().
"""


def read_file(filename=""):
    """
        Reads a file and prints it
        filename : file to open
    """
    with open('my_file_0.txt', encoding="utf-8") as file:
        print(f"{file.read()}", end="")
