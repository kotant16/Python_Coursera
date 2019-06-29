x0 = int(input())
y0 = int(input())
x1 = int(input())
y1 = int(input())

test_set = [(x0, y0, x1, y1)]


def emulate(coordinates):

    x0, y0, x1, y1 = coordinates

    conditions = ([(x1 + y1) % 2 == (x0 + y0) % 2 == 0,  # should be on black
                   y1 - y0 > 0,  # straightforward
                   abs(x1 - x0) <= y1 - y0,  # can be reachable
                   0 < max(coordinates) <= 8  # in range
                   ])

    if all(conditions):
        print('YES')
    else:
        print('NO')


for coordinates in test_set:
    # print(coordinates)
    emulate(coordinates)
