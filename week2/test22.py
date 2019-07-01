k = int(input())
m = int(input())
n = int(input())
t = 0

if k >= n:
    t = m * 2

elif n % k == 0:
    t = ((n // k) * m * 2)

elif n % k != 0:
    if (n % k) > (k / 2):
        t = ((n // k) * m * 2) + m * 2
    elif (n % k) < (k / 2):
        t = (((n // k)) * m * 2) + m
print(t)
