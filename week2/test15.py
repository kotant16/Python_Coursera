a = int(input())
b = int(input())
c = int(input())

if a != b and b != c and c != a:
    print(0)
elif a == b and b != c:
    if a != c:
        print(2)
elif a != b and b == c:
    if a != c:
        print(2)
elif a != b and b != c:
    if a == c:
        print(2)
else:
    print(3)
