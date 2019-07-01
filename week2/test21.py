a = int(input())
b = int(input())
c = int(input())
d = int(input())

# def solver(a, b, c, d):
if (a != 0) & (b*c-a*d != 0):
    x = -b/a
    if (x == round(x)) & ((c*x+d) != 0):
        print(int(-b/a))
    else:
        print('NO')
elif a == 0 & b == 0:
    print('INF')
else:
    print('NO')

