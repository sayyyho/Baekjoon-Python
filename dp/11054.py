n = int(input())
data = list(map(int, input().split()))
max_dp = [1 for _ in range(n)]
min_dp = [1 for _ in range(n)]
up_down_dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            max_dp[i] = max(max_dp[j]+1, max_dp[i])
        if data[i] < data[j]:
            min_dp[i] = max(min_dp[j]+1, min_dp[i])
            up_down_dp[i] = max(up_down_dp[j]+1, max_dp[j]+1, up_down_dp[i])
            
find_maxpoint = max(max_dp)
find_minpoint = max(min_dp)
find_updown = max(up_down_dp)
print(max(find_maxpoint,find_minpoint,find_updown))