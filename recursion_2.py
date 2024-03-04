#!/usr/bin/python3

def isArrayInSortedOrder(A):
    """
    Check if the array is in sorted order
    with Recursion.
    """
    if len(A) == 1:
        return True
    return A[0] <= A[1] and isArrayInSortedOrder(A[1:])


arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(isArrayInSortedOrder(arr))
