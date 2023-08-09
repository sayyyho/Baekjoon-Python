import sys; input = sys.stdin.readline

n, k = map(int, input().split())

data = [i for i in range(1, n+1)]
result = []

now = k

while data:
    length = len(data)
    if now > length: 
        while now > length: now -= length
    result.append(data[now-1])
    del data[now-1]
    now += k - 1
print("<", end="")
print(*result, sep=", ", end="")
print(">")
