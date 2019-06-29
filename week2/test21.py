a = int(input())
b = int(input())
c = int(input())
d = int(input())

# def solver(a, b, c, d):
A = (a == 0 & b == 0)  # first line in 0
# B = a!=0 # first line not parallel
C = (a == 0 & b != 0)  # first line parallel
D = (c == 0 & d == 0)  # second line in zero
E = (b / a == d / c)  # both lines intersects in one point

if any([A]):
    print('INF')
elif any([E, C, D]):
    print('NO')
else:
    print(int(-b / a))
