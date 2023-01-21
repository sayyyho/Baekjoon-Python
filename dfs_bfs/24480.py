import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

count = 0
num_v, num_e, s = map(int, input().split())
graph = [[] for _ in range(num_v+1)]
visited = [False for _ in range(num_v+1)]
result = [0 for _ in range(num_v+1)]

for _ in range(num_e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, num_v+1):graph[i].sort(reverse=True)

def dfs(s):
    global count
    count += 1
    visited[s] = True
    result[s] = count
    for search in graph[s]:
        if not visited[search]:
            dfs(search)
    return

dfs(s)
print(*result[1:], sep="\n")