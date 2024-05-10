#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_arguments = len(sys.argv) - 1

    print(f"Number of argument{'s' if num_arguments != 1 else ''}: {'.' if num_arguments == 0 else ''}")

    if num_arguments > 0:
        for i in range(1, num_arguments + 1):
            print(f"{i}: {sys.argv[i]}")

