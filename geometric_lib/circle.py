import math

def area(r):
    '''
    Принимает радиус круга r (float или int).
    Возвращает площадь круга (float),
    вычисляемую по формуле: π * r².
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Принимает радиус круга r (float или int).
    Возвращает длину окружности (float),
    вычисляемую по формуле: 2 * π * r.
    '''
    return 2 * math.pi * r

print(perimeter(5))
