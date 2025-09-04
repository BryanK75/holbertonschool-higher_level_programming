#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        end_char = ", " if not (i == 8 and j == 9) else "\n"
        print("{}{}".format(i, j), end=end_char)
