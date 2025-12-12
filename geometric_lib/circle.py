import math

def _validate(r):
    if not isinstance(r, (int, float)):
        raise TypeError("Radius must be numeric")
    if r < 0:
        raise ValueError("Radius must be non-negative")


def area(r):
    _validate(r)
    return math.pi * r * r


def perimeter(r):
    _validate(r)
    return 2 * math.pi * r
