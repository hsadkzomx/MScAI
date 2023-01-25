def invert_dict(d):
    """Use a dict comprehension to invert the dict.

    >>> invert_dict({"a": 1, "dog": 3, "giraffe": 7})
    {1: 'a', 3: 'dog', 7: 'giraffe'}
    
    """
    
    # your code here
    # recall "for k in d" iterates over the keys of d


import doctest
doctest.testmod(verbose=True)
