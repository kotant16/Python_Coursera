A = int(input())
B = int(input())
N = int(input())
totalCost = N*(A*100 + B)  # type: int
print(totalCost // 100, totalCost % 100)
