#!/usr/bin/python3
"""
Resolve minimum operations to get # of leters with just
copy and paste operations
"""

def minOperations(n):
    """ Get all the common divisors,
        store them in a list
        return the sum of list numbers
    """
    if n < 2:
        return 0
    x = 2
    y = n
    numbs = []
    while y > 1:
        if (y/x).is_integer():
            y /= x
            numbs.append(x)
        else:
            x += 1
    return int(sum(numbs))