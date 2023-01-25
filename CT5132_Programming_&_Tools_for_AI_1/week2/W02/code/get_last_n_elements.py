def get_last_n_elements(s, n):
    """
    >>> get_last_n_elements("abcde", 2)
    'de'

    >>> get_last_n_elements("abcde", 7) # notice we can write doctests to expect errors, as here:
    Traceback (most recent call last):
        ...
    ValueError: Can't return 7 elements from abcde of length 5
    """

    # your code here

    
import doctest
doctest.testmod(verbose=True)

