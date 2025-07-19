def ft_filter(function, iterable):
    """
    Recreate the behavior of the built-in filter() function.

    Args:
        function: A function that returns True or False
        iterable: An iterable object to filter

    Returns:
        An iterator over items for which function returns True
    """
    return iter([item for item in iterable if function(item)])
