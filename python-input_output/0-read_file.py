#!/usr/bin/python3
"""
File function for read_file().
"""

def read_file(filename=""):
    """
    Reads a file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to open and read. Default is an empty string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")

# Example usage:
# read_file("example.txt")
