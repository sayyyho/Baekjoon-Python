# 한 번 더 풀어보기
n,m = map(int,input().split())
s = []
 
def backtracking():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1): # 9-10번째 줄이 backtracking의 핵심 > 모두 확인하면서 유효성 검사를 하기때문.
        if i not in s: 
            s.append(i)
            backtracking()
            s.pop()
backtracking()