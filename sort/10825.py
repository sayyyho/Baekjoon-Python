import sys
input = sys.stdin.readline
n = int(input())
data = []

for i in range(n):
    data.append(list(input().split()))
    data[i][1] = int(data[i][1])
    data[i][2] = int(data[i][2])
    data[i][3] = int(data[i][3])
data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for value in data: print(value[0])