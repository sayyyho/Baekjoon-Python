n = int(input())
datas = []
for _ in range(n):
    age, name = input().split()
    datas.append([int(age), name])
datas.sort(key=lambda x: x[0])
for data in datas:print(data[0], data[1])