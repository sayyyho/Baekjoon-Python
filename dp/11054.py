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

# 다른 사람들 발상
# 감소 배열을 역전시켜서 특정 i까지의 증가 배열의 dp + 감소 배열의 dp합을 새로운 배열로 정의한 뒤 그 중 최대값 뽑기
# import sys
# n = int(sys.stdin.readline())
# s = list(map(int,sys.stdin.readline().split()))
# up = [1]*n
# down = [0]*n
# for i in range(1,n):
#     for j in range(i):
#         if s[j]<s[i]:
#             up[i] = max(up[j]+1,up[i])
 
# for i in range(n-1,-1,-1):
#     for j in range(i,n):
#         if s[i]>s[j]:
#             down[i] = max(down[j]+1,down[i])
 
# sum =0
# for i in range(n):
#     sum = max(sum,up[i]+down[i])
 
# print(up,down)
# print(sum)