def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, otherwise False.

    Args:
        obj: Any Python object
        a_class: The class to compare with

    Returns:
        True if obj is exactly an instance of a_class, False otherwise
    """
    return type(obj) is a_class
