import sys

n = int(input())
datas = []

for _ in range(n):datas.append(sys.stdin.readline().strip())

datas = list(set(datas))
datas.sort()
datas.sort(key=len)

for data in datas:print(data)