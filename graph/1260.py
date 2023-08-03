 #set 선언 : iterable한 list를 통해
from collections import deque

def dfs(visited, now, data):
    if (visited[now] == True):
        return
    visited[now] = True
    print(now, end=" ")
    for search in data[now]:
        if not visited[search]:
            dfs(visited, search, data)
    return

def bfs(visited, start, data):
    queue = deque([start])
    visited[start] = True
    while queue:
        value = queue.popleft()
        print(value, end=' ')
        for i in data[value]:    
            if not visited[i]:
                queue.append(i)
                visited[i] = True

vertex, edge, start = map(int, input().split())
visited1 = [False]* (vertex + 1)
visited2 = [False]* (vertex + 1)
data = [[] * (vertex + 1) for _ in range(vertex + 1)]
for i in range(edge):
    node1, node2 = map(int, input().split())
    data[node1].append(node2)
    data[node2].append(node1)
    data[node1].sort()
    data[node2].sort()

dfs(visited1, start, data)
print()
bfs(visited2, start, data)
