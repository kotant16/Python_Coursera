import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())

# print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")

m = int(a * c)
k = int(a * d) + int(b * c)
n = int(b * d)

# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))

diScr = k ** 2 - 4 * m * n
print(diScr)

if diScr < 0:
    print("NO")

elif diScr == 0:
    x = -k / (2 * a)
    print(x)
else:
    x1 = int((-k + math.sqrt(diScr)) / (2 * m))
    x2 = int((-k - math.sqrt(diScr)) / (2 * m))
    print(x1, x2)

