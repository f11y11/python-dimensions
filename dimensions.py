def dimensions(
    __list:List[Any]
    ):
    """
    Returns the dimensions of a given list
    ### Example:
    >>> dimensions([1,2,3])
    ... 1
    >>> dimensions([[1,2,3], [4,5,6], [7,8,9]])
    ... 2
    >>> dimensions([[[[1]], [[2]], [[3]]])
    ... 3

    ### Notes:
    Every iteration that only contains another group of lists
    will be considered a dimension.
    
    The longest list in the current iteration will be used in the next iteration
    """
    dims = 1
    nextiter = __list
    while True:
        items = [item for item in nextiter]
        if all(
            [isinstance(item, List) for item in items]
            ):
            dims += 1
            lsizes = tuple(len(item) for item in items)
            nextiter = items[lsizes.index(max(lsizes))]
            continue
        else:
            return dims
