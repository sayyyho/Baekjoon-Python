n = int(input())
data = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if data[i] > data[j]: dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))