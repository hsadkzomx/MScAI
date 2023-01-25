import numpy as np

def broadcastable(x, y):
    """Return True or False, indicating whether the arrays x and y can be broadcast together.
    Assume x and y are both Numpy arrays.

    For each doctest, you can also paste the inputs x and y and calculate (eg) x + y in IPython.
    Where we have True below, you should get a result. Where we have False below, you
    should see a message such as:
    "ValueError: operands could not be broadcast together with shapes (2,3) (2,)"
    

    >>> broadcastable(np.array([4, 1, 2]), np.array([1, 4, 7]))
    True

    >>> broadcastable(np.array([4, 1, 2]), np.array([18]))
    True

    >>> broadcastable(np.array([4, 1, 2]), np.array([1, 18]))
    False
    
    >>> broadcastable(np.array([[4, 1, 2],
    ...                         [5, 5, 5]]),
    ...               np.array([1, 8, 7]))
    False

    >>> broadcastable(np.array([[4, 1, 2],
    ...                         [5, 5, 5]]),
    ...               np.array([1, 7]))
    True
    
    >>> broadcastable(np.array([[4, 1, 2],
    ...                         [5, 5, 5]]),
    ...               np.array([[1, 8, 7]]))
    True

    
    """

    # if x.shape is longer than y.shape (or vice versa)
    # then zip will just discard. Because we use reversed()
    # we consider the shapes starting from the right as required by
    # the rules.
    
    # print(x.shape)
    # print(y.shape)
    for xi, yi in reversed(list(zip(x.shape, y.shape))):
        # print(xi, yi)
        if xi == yi: # if equal, this pair is ok
            continue
        if xi == 1: # if one of the items equals 1, this pair is ok
            continue
        if yi == 1:
            continue
        return False # otherwise, it's bad and we return False
    
    return True # if all pairs ok, then the shapes are ok

