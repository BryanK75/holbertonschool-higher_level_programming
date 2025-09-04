#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]  # exclude the script name
    total = 0

    for arg in argv:
        total += int(arg)

    print(total)
