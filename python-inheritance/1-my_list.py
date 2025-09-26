class MyList(list):
    """A list subclass with a method to print a sorted version of the list."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
