n = int(input())
dp = [[1 for _ in range(10)] for _ in range(n+1)] # 오르막수

for i in range(2,n+1):
    for j in range(9,0,-1):
        for k in range(1,j+1):
            dp[i][j] += dp[i-1][k] % 10007
print(sum(dp[n]) % 10007)