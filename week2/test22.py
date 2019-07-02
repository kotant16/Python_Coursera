k = input()
m = input()
n = input()

if min(k, m, n) <= 0:
    print(0)
sides = n*2
cycles = sides//k
if sides%n == 0:
    print(cycles*m)
else:
    print(cycles*m + m)
