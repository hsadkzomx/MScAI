def invert_dict(d):
    """Use a dict comprehension to invert the dict.

    >>> invert_dict({"a": 1, "dog": 3, "giraffe": 7})
    {1: 'a', 3: 'dog', 7: 'giraffe'}
    
    Recall keys must be unique. If we have a dict with non-unique *values* and
    we invert, we'll now have non-unique keys, so the *later* ones will over-write
    the earlier ones. Notice *dog* disappears:
    
    >>> invert_dict({"a": 1, "dog": 3, "giraffe": 7, "cat": 3}) 
    {1: 'a', 3: 'cat', 7: 'giraffe'}

    
    """
    
    # remember, "for k in d" iterates over the keys of the dict.
    return {d[k]: k for k in d}


import doctest
doctest.testmod(verbose=True)
