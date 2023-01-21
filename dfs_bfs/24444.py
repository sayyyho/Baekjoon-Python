import sys
from collections import deque

v, e, start = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]
path = deque()
result = [0 for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, v+1):graph[i].sort()

def bfs(now):
    path.append(now)
    count = 1
    visited[now] = True
    while path:
        now = path[0]
        result[now] = count
        for vertex in graph[now]:
            if visited[vertex] == False: 
                path.append(vertex)
                visited[vertex] = True
        path.popleft() 
        count+=1
bfs(start)

for i in range(1, v+1): print(result[i])