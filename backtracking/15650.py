n,r = map(int, input().split())
res = [0]

def dfs():
    if (len(res) == r and res[0] != 0):
        print(' '.join(map(str, res)))
        return
    for i in range(1, n+1): 
        if i > res[-1]:
            if (res[-1] == 0):
                res.pop()
            res.append(i)
            dfs()
            res.pop()
            if (len(res) == 0):
                res.append(0)
dfs()
