n = int(input())
print('%01d:%02d:%02d' % (n // 3600 % 24, n // 60 % 60, n % 60))
