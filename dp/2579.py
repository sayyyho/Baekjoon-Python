n = int(input())
data = [0]
for _ in range(n):
    data.append(int(input()))
if n == 1: print(data[1])
elif n == 2: print(data[1] + data[2])
else:
    dp = [0 for _ in range(n+1)]
    dp[1] = data[1]
    dp[2] = data[1] + data[2]
    for i in range(3,n+1):
        dp[i] = max(dp[i-2] + data[i], dp[i-3] + data[i-1] + data[i])
    print(dp[-1])