import sys
sys.setrecursionlimit(10000)

def ctr_visit(i, j):
    visited[i][j] = True
    i_flag = 0
    j_flag = 0
    if i < 0 or i > n - 1: i_flag = 1
    if j < 0 or j > m - 1: j_flag = 1
    if i > 0 and j_flag == 0:
        if data[i-1][j] == 1 and visited[i-1][j] == False: ctr_visit(i-1, j)    
    if i < n - 1 and j_flag == 0:
        if data[i+1][j] == 1 and visited[i+1][j] == False: ctr_visit(i+1, j) 
    if j > 0 and i_flag == 0:
        if data[i][j-1] == 1 and visited[i][j-1] == False: ctr_visit(i, j-1)    
    if j < m - 1 and i_flag == 0:
        if data[i][j+1] == 1 and visited[i][j+1] == False: ctr_visit(i, j+1)    
    return

n = int(input())
for _ in range(n):
    n, m, k = map(int, input().split())
    data = [[0 for _ in range(m)]for _ in range(n)]
    visited = [[False for _ in range(m)]for _ in range(n)]
    for _ in range(k):
        row, col = map(int, input().split())
        data[row][col] = 1
    # check 할 곳 찾기
    cnt = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1 and visited[i][j] == False: 
                ctr_visit(i, j)
                cnt += 1            
    print(cnt)