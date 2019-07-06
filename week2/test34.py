n = int(input())
count = 0
seqSum = n
while n != 0:
    n = int(input())
    count += 1
    seqSum = seqSum + n
print(float(seqSum / count))
######
