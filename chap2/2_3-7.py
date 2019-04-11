def sumOf2isX(s, x):
    """ determine whether or not there exist two elements in s whose sum is x.
    s: a sorted set.
    x: value we are looking for.
    
    >>> s = [1, 3]
    >>> sumOf2isX(s, 4)
    True
    >>> sumOf2isX(s, 8)
    False
    """
    # before we start, check some sicuations.
    if len(s) == 1:
        return False
    
    for i in range(0, len(s)):
        another_key = x - s[i]
        left = 0
        right = len(s) - 1
        mid = (left + right)//2
        while left <= right:
            if another_key < s[mid]:
                right = mid - 1
                mid = (left + right) // 2
            elif another_key > s[mid]:
                left = mid + 1
                mid = (left + right) // 2
            else:
                if mid == i:
                    continue
                return True
    return False