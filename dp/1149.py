n = int(input())
result = 0
data = []
min_data = []
path = []
for i in range(n):
    data.append(list(map(int, input().split())))
    min_data.append(min(data[i]))
    path.append(data[i].index(min(data[i])))

for i in range(2, n-1):
    if(path[i]==path[i+1]):
        if(min_data[i]<=min_data[i+1]):
            data[i+1][path[i+1]] = max(data[i+1])+1
            data[i+1][path[i-1]] = max(data[i+1])
            min_data[i+1] = min(data[i+1])
            path[i+1] = data[i+1].index(min(data[i+1])) 
        else:
            data[i][path[i]] = max(data[i])+1
            data[i][path[i-1]] = max(data[i])
            min_data[i] = min(data[i])
            path[i] = data[i].index(min(data[i])) 

print(min_data)
print(sum(min_data))
# 이전까지의 합들이 최소값이라는 보장이 없음

# 8
# 71 39 44
# 32 83 55
# 51 37 63
# 89 29 100
# 83 58 11
# 65 13 15
# 47 25 29
# 60 66 19