"""
Module for experimenting with lower and upper bounds.

Unlike in the BED functionality, where we need to search for a lower bound in
a list of features, here we only concern ourselves with lists of integers.
"""


def lower_bound(x: list[int], v: int) -> int:
    """Get the index of the lower bound of v in x.

    If all values in x are smaller than v, return len(x).
    """
    # binary search to find v in x
    low, high = 0, len(x)
    while low < high:
        mid = (low + high) // 2
                                      # keep looking, to find potential earlier indexed v
        if x[mid] < v:
            low = mid + 1
        else:
            high = mid

    return low

def upper_bound(x: list[int], v: int) -> int:
    """Get the index of the upper bound of v in x.

    If all values in x are smaller than v, return len(x).
    """
    return lower_bound(x, v+1)             # upper bound for v is the lower bound for number 1 higher than v


