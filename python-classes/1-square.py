#!/usr/bin/python3
"""Class Square that defines a square by its size."""


class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size):
        """Initialize the square with a given size.
        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size
