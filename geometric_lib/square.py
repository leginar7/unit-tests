def _validate(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Side must be numeric")
    if a < 0:
        raise ValueError("Side must be non-negative")


def area(a):
    _validate(a)
    return a * a


def perimeter(a):
    _validate(a)
    return 4 * a
