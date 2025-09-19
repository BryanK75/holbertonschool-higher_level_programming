#!/usr/bin/python3
"""Class Square that defines a square by its size with validation."""


class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize the square with an optional size.
        Args:
            size (int): The size of the square (must be >= 0).
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
