def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or an instance of a subclass of a_class.

    Args:
        obj: Any Python object
        a_class: The class to compare with

    Returns:
        True if obj is an instance of a_class or subclass, False otherwise
    """
    return isinstance(obj, a_class)
