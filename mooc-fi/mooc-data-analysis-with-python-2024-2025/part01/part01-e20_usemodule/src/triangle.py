import math

__version__ = """1.0"""
__author__ = """Isaul"""
__doc__ = """This is the documentation."""

def hypotenuse(a, b):
    """
    Returns the length of the hypotenuse of a right-angled triangle.
    """
    return math.sqrt(a ** 2 + b ** 2)

def area(a, b):
    """
    Returns the area of a right-angled triangle.
    """
    return 0.5 * a * b

