#!/usr/bin/python3
"""Class Square that defines a square by its size and position."""


class Square:
    """Defines a square with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with optional size and position.
        Args:
            size (int): The size of the square (must be >= 0).
            position (tuple): The position offset (must be a tuple of 2 positive integers).
        """
        self.size = size          # validate via setter
        self.position = position  # validate via setter

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #.
        If size is 0, print an empty line.
        Position is used to offset the square.
        """
        if self.__size == 0:
            print("")
            return

        # move down by position[1]
        for _ in range(self.__position[1]):
            print("")

        # print each row with leading spaces (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
