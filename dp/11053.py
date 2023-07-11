# n = int(input())
# data = list(map(int, input().split()))
# dp = [1 for _ in range(n)]

# if n == 1: print(1)
# elif n == 2: print(2) if data[0] < data[1] else print(1)
# else:
#     memo = list()
#     memo.append(data[0])
#     for i in range(1, n):
#         if memo[-1] < data[i]: 
#             memo.append(data[i])
#             dp[i] = dp[i-1] + 1
#         else:
#             if dp[i-1] <= dp[i] and memo[0] > data[i]:
#                 memo = [data[i]]
#                 dp[i] = 1
#             elif n - i >= n//2 and memo[-1] > data[i] and memo[-2] != data[i]:
#                 while (data[i] < memo[-1]): 
#                     memo.pop()
#                     if len(memo) == 0: break
#                 memo.append(data[i])
#                 dp[i] = len(memo) 
#             else:
#                 dp[i] = dp[i-1] 
#         print(memo)
#     print(dp[n-1])
# 다시 !!!!