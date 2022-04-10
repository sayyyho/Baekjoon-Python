# 결과들의 규칙성이 있는지 파악하면 풀리는 문제

N = int(input())
dp = [0] * 1000001
dp[1] , dp[2] = 1, 2
for i in range(3, N+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746
print(dp[N])
