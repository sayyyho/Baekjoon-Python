trial = int(input())

def dp(n):
    if (n < 4): return 1
    triangle = [0 for _ in range(n+1)]
    triangle[1] = 1
    triangle[2] = 1
    triangle[3] = 1
    for i in range(4, n+1):
        triangle[i] = (triangle[i-3] + triangle[i-2]) 
    return(triangle[n])

for _ in range(trial):
    n = int(input())
    print(dp(n))