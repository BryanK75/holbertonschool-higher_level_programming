#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited (directly or indirectly)
    from a_class, otherwise False.

    Args:
        obj: Any Python object
        a_class: The class to compare with

    Returns:
        True if obj inherits from a_class, False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
