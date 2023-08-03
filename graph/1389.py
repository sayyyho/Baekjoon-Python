import sys; input = sys.stdin.readline
from collections import deque

user, line = map(int, input().split())
data = [[] for _ in range(user + 1)]
result = list()

def bfs(start, visited):
    queue = deque([[start, 0]])
    visited[start] = True
    result = 0
    while queue:
        value = queue.popleft()
        result += value[1]
        for i in data[value[0]]:    
            if not visited[i]:
                queue.append([i, value[1] + 1])
                visited[i] = True
    return result

for _ in range(line):
    n, m = map(int, input().split())
    data[n].append(m)
    data[m].append(n)

for i in range(1, user + 1):
    result.append(bfs(i, [False for _ in range(user + 1)]))

print(result.index(min(result)) + 1)