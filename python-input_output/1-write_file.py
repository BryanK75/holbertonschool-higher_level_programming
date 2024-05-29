#!/usr/bin/python3
"""
    Writes a string to a text file and returns the number of characters written

    Args:
        filename(str): The name of the file to write to.

        text(str): The string to write to the file. Default is an empty string

    Returns:
        int: The number of characters written to the file.
"""


def write_file(filename="", text=""):
    with open('my_first_file.txt', 'w', encoding="utf-8") as f:
        return f.write(text)

# example usage:
# print(write_file("example.txt", "Hello, World!")) # Outputs: 13

