def Binsearch(A, value):
    """ 
    Binary Search
    A:     an increasing sorted array.
    size:  size of array.
    value: the value which need to be find.
    >>> s = [5, 13]
    >>> Binsearch(s, 5)
    0
    >>> Binsearch(s, 13)
    1
    >>> Binsearch(s, 18)
    """
    #
    # bounds for the both side and the middle bound.
    # 
    l = 0
    r = len(A) - 1
    mid = (l + r) // 2
    while l <= r:
        if value > A[mid]:
            l = mid + 1
            mid = (r + l) //2
        elif value < A[mid]:
            r = mid - 1
            mid = (r + l) //2
        else:
            return mid