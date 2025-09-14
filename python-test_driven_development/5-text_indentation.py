#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    end_chars = {'.', '?', ':'}
    line = ""
    for char in text:
        line += char
        if char in end_chars:
            print(line.strip())
            print()
            line = ""
    if line:
        print(line.strip())
