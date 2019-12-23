class GlobalPlaceholder:
    """
    Global placeholder to avoid circular imports
    """
    __slots__ = ['db']


Global = GlobalPlaceholder()