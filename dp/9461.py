dp = [0] * 102
dp[0], dp[1], dp[2] ,dp[3], dp[4] = 0, 1, 1, 1, 2

T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(5, N+1):
        if(dp[i]):
            continue
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[N])

