n = int(input())
dp = [0] * 1000002

dp[2] = 1
dp[3] = 1 

for i in range(4,n+1):
    if i % 6 == 0:
        dp[i] = dp[i//3] + 1 if dp[i//3] + 1 < dp[i//2] + 1 else dp[i//2] + 1
    elif i % 3 == 0: dp[i] = dp[i // 3] + 1
    elif i % 2 == 0: dp[i] = dp[i // 2] + 1
    if dp[i] == 0: dp[i] = dp[i-1] + 1
    else: dp[i] = min(dp[i], dp[i-1] + 1)
print(dp[n])


# vkdldjvkdnj(29등) 코드
# X = int(input())
# dp = [0 for _ in range(X + 1)]
# for i in range(2, X + 1):
#     if i == 2:
#         dp[i] = 1
#     elif i == 3:
#         dp[i] = 1
#     else:
#         dp[i] = dp[i - 1] + 1
#         if not i % 3:
#             dp[i] = min(dp[i], dp[i // 3] + 1)
#         if not i % 2:
#             dp[i] = min(dp[i], dp[i // 2] + 1)
# print(dp[X])