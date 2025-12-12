def _validate(a, b, c=None):
    # area uses 2 params
    if c is None:
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Sides must be numeric")
        if a < 0 or b < 0:
            raise ValueError("Sides must be non-negative")
        return

    # perimeter uses 3 params
    if not (
        isinstance(a, (int, float))
        and isinstance(b, (int, float))
        and isinstance(c, (int, float))
    ):
        raise TypeError("Sides must be numeric")
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Sides must be non-negative")


def area(a, b):
    _validate(a, b)
    return 0.5 * a * b


def perimeter(a, b, c):
    _validate(a, b, c)
    return a + b + c
