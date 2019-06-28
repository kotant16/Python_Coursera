from itertools import permutations

w = int(input())
k = int(input())
h = int(input())
a1 = int(input())
a2 = int(input())
a3 = int(input())


def check_volume(w, k, h, a1, a2, a3):
    return (w//a1) * (k//a2) * (h//a3)


def check_capacity(w, k, h, a1, a2, a3):
    variants = list(permutations([a1, a2, a3]))
    print(max([check_volume(w, k, h, *args) for args in variants]))


check_capacity(w, k, h, a1, a2, a3)
