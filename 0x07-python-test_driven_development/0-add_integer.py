#!/usr/bin/python3
"""
Module for add_integer method.
it adds two integers.
a and b must be integers
"""


def add_integer(a, b=98):
    """Adds two integers.
    Return an integer: sum of a and b.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
