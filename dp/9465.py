test_case = int(input())

for _ in range(test_case):
    n = int(input())
    data = list()
    for _ in range(2): data.append(list(map(int, input().split())))
    if n == 1: print(max(data[0][0], data[1][0]))
    elif n == 2: print(max(data[0][0] + data[1][1], data[1][0] + data[0][1]))
    else:
        dp = [[0 for _ in range(n)] for _ in range(2)]
        dp[0][0] = data[0][0]
        dp[1][0] = data[1][0]
        dp[0][1] = dp[1][0] + data[0][1]
        dp[1][1] = dp[0][0] + data[1][1] 
        for i in range(2,n):
            dp[0][i] = data[0][i] + max(dp[1][i-1], dp[1][i-2]) 
            dp[1][i] = data[1][i] + max(dp[0][i-1], dp[0][i-2])
        print(max(dp[0][-1], dp[1][-1]))
# 아이디어는 맞지만, 구현 참고