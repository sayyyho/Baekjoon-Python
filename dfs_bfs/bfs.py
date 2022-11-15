from collections import deque

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