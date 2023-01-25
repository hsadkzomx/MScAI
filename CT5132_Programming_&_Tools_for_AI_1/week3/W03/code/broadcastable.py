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

    return False # replace with your code

