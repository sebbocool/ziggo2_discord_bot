def to_int(value: any, default: int = 0):
    """
    Convert a given value to an int or return a default value if conversion fails.
    :param value: The value to be converted.
    :param default: The default value to return if conversion fails. Defaults to 0.
    :return: The parsed int or default value.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return default
