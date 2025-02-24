def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable
    for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function is None:
        return [i for i in iterable]
    return [i for i in iterable if function(i)]
