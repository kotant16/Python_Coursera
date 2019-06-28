# Тренировочное задание по программированию: Симметричное число*
V = int(input())
a = int(V / 1000)
s = int(V / 100 % 10)
d = int(V / 10 % 10)
f = int(V % 10)
t = int((a - f) * (a - f) + (s - d) * (s - d) + 1)
# print(a, s, d, f)
if t == 1:
    print(t)
else:
    print(0)
