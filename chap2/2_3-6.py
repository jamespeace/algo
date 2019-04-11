def insertionSort(A):
    """ Insertion sort
    >>> s = [1, 2, 3]
    >>> insertionSort(s)
    >>> s
    [1, 2, 3]
    """
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[j] into the sorted sequence A[0..j-1]
        right = j - 1
        left = 0
        mid = (left + right) // 2
        index_put = j
        # Using binary search to search the place to plug into.
        while right <= left < j:
            if key < A[mid]:
                right = mid - 1
                index_put = right
                mid = (left + right) // 2
            else:
                left = mid + 1
                index_put = left
                mid = (left + right) // 2
            
        # literlly move the element to the left.
        for element in range(j, index_put, -1):
            A[element] = A[element-1]
        A[index_put] = key
        print(s)

s = [1, 2, 3]
insertionSort(s)