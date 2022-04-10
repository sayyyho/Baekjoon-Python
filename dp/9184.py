dp = [[0]*10 for _ in range(10)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0: # 하나라도 0이하일 경우
        return 1
    if a > 20 or b > 20 or c > 20: #하나라도 20보다 큰 경우
        return w(20, 20, 20)
    if (dp[a][b][c]):
        return dp[a][b][c]
    if a < b and b < c: #오름차순 정렬된 경우
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c) # c부터 끝장 + b랑 c줄이기 - b만 줄인거 
        return dp[a][b][c]
    else: # 다 아닌경우 
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]

while (True):
    a, b, c = map(int, input().split())
    if (a == -1 and b == -1 and c == -1):
        break
    print("w({}, {}, {}) = {}".format(a,b,c, w(a,b,c)))