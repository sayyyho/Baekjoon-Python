n = int(input())
info = list()

for _ in range(n): info.append(list(map(int, input().split())))

ranking = list()

for value in info:
    count = 1
    for opponent in info:
        if value[0] < opponent[0] and value[1] < opponent[1]: count += 1
    ranking.append(count)
    
print(*ranking)
                