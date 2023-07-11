n = int(input())
data = list(map(int, input().split()))
dp = [0 for _ in range(n)]
# dp : 현재 번호에서 체크한 최대값 배열

dp[0] = data[0]
check_index = 0

for i in range(1,n): # 배열 전체 다 돌려보자
    for j in range(0,i+1): # 지금 선택한 배열 인덱스에서,,
        now = 0
        bf = -1
        for k in range(j,i+1): 
            if data[k] > bf:
                now += data[k]
                bf = data[k]
        if now >= dp[i]:
            bf = -1
            for index in range(j):
                if data[index] < data[j]: 
                    now += data[index]
            dp[i] = now            
print(max(dp))
    
    # if data[i] > data[check_index]: 
    #     dp[i] = dp[i-1] + data[i]
    #     check_index = i
    # else:
    #     now = -1
    #     total = 0
    #     for j in range(i+1):
    #         if j == check_index or data[j] <= now: continue
    #         else: 
    #             total += data[j]
    #             now = data[j]
    #     if total > dp[i-1]: dp[i] = total
    #     else: dp[i] = dp[i-1]            
# print(dp[-1])
        