# 내 코드 -> 틀림

n = int(input())

dp = [0 for _ in range(101)]

dp[1] = 9
dp[2] = 17
loss = 2
for i in range(3, n+1):
    dp[i] = 2 * dp[i-1] - loss
    loss += (2*i - 5) 

print(dp[n] % 1000000000)


# dp[i][j] = (i자리 숫자이면서 j로 시작하는 수의 개수)로 생각해보세요.

# N = int(input())
# dp = [[0,0,0,0,0,0,0,0,0,0]] * (N+1)
# dp = [[0] * 10 for _ in range(N+1)]
# dp[1] = [0,1,1,1,1,1,1,1,1,1]
# for i in range(2,N+1):
#     dp[i][0] = dp[i-1][1]
#     dp[i][9] = dp[i-1][8]
#     for j in range(1,9):
#         dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
#     print("{}번째 dp : {}".format(i, dp))
# print(sum(dp[-1])%1000000000)