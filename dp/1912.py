import sys

n = int(input())
dp = [0 for _ in range(n)]
data = list(map(int, sys.stdin.readline().split()))
dp[0] = data[0]
my_max = dp[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + data[i], data[i])
    if(my_max<dp[i]):my_max = dp[i]
print(my_max)


