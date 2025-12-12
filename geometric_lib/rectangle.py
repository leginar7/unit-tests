def _validate(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Sides must be numeric")
    if a < 0 or b < 0:
        raise ValueError("Sides must be non-negative")


def area(a, b):
    _validate(a, b)
    return a * b


def perimeter(a, b):
    _validate(a, b)
    return 2 * (a + b)
