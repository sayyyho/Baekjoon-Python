n = int(input())
data1 = list(map(int, input().split()))
m = int(input())
data2 = list(map(int, input().split()))
data1.sort()

for now in data2:
    if now in data1: print(1)
    else: print(0)