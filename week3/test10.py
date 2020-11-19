import math
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4 * a * c
eps = 1.0e-9
if d >= eps:
    x1 = (-b - math.sqrt(d)) / 2 / a
    x2 = (-b + math.sqrt(d)) / 2 / a
    if x1 > x2:
        print(2, x2, x1)
    elif x1 < x2:
        print(2, x1, x2)
    else:
        print(3)
elif abs(d) < eps:
    x1 = -b / 2 / a
    print(1, x1)
