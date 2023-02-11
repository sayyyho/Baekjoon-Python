n = int(input())
datas = []

for i in range(n): datas.append(list(map(int, input().split())))

datas.sort(key=lambda x: (x[0],x[1]))

for data in datas: print(*data)