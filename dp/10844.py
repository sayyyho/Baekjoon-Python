n = int(input())
# dp[n][m] 길이 n에서 m으로 끝나는 개수 즉, 각 요소를 다 더하면 n에서 총 개수가 나옴
dp = [[] for _ in range(n+1)]
dp[0] = [0] * 10
dp[1] = [0,1,1,1,1,1,1,1,1,1]


for i in range(2,n+1):
    for j in range(10):
        if j == 0:
            dp[i].append(dp[i-1][1])
        elif j == 9:
            dp[i].append(dp[i-1][8])
        else:
            dp[i].append(dp[i-1][j-1] + dp[i-1][j+1])
print(sum(dp[n])%1000000000)