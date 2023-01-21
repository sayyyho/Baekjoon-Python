import sys
from collections import deque

input = sys.stdin.readline

computer = int(input())
network = int(input())
datas = [[] for _ in range(computer+1)]
check = [False for _ in range(computer+1)]

for _ in range(network):
    c1, c2 = map(int, input().split())
    datas[c1].append(c2)
    datas[c2].append(c1)

def bfs():
    result = 0
    path = deque()
    now = 1 
    path.append(now)
    check[now] = True
    while path:
        now = path[0]
        for data in datas[now]:
            if not check[data]: 
                path.append(data)
                check[data] = True
        path.popleft()
        result+=1
    return result

result = bfs()
print(result - 1)