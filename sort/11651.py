n = int(input())

data = list()

for _ in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: (x[1],x[0]))

for value in data: print(value[0], value[1])