n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

for k in range(1, n):
    tri[k][0] += tri[k-1][0]
    tri[k][k] += tri[k-1][k-1]
    for i in range(1,k):
        tri[k][i] += max(tri[k-1][i-1], tri[k-1][i])
print(max(tri[n-1]))