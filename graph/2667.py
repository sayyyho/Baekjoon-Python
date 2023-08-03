import sys

count = 0
input = sys.stdin.readline

n = int(input())

visited = [[False] * (n+2) for _ in range(n+2)]
graph = [[0]*(n+2) for _ in range(n+2)]

for i in range(1, n+1):
    graph[i] = list(map(int, str(("0" + input().strip() + "0"))))


def start():
    result = []
    check = 0
    global count
    for i in range(1, n+1):
        for j in range(1, n+1):
            if not visited[i][j] and graph[i][j] == 1:
                check += 1
                dfs(i, j)
                result.append(count)
                count = 0
    print(check)
    result.sort()
    print(*result, sep="\n")

def dfs(i, j):
    global count
    count +=1
    visited[i][j] = True
    if graph[i-1][j] == 1 and not visited[i-1][j]:
        dfs(i-1, j)
    if graph[i+1][j] == 1 and not visited[i+1][j]:
        dfs(i+1, j)
    if graph[i][j-1] == 1 and not visited[i][j-1]:
        dfs(i, j-1)
    if graph[i][j+1] == 1 and not visited[i][j+1]:
        dfs(i, j+1)
    return
    
start()