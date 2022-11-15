T = int(input())
for _ in range(T):
     x,y,r,a,b,c = map(int, input().split())  
     if (x == a and y == b and r == c):print(-1)
     elif((r + c)**2 == (x-a)**2 + (y-b)**2):print(1)
     elif((r - c)**2 == (x-a)**2 + (y-b)**2):print(1) #내접 놓침
     elif((r - c)**2 < (x-a)**2 + (y-b)**2 < (r + c)**2):print(2) #두점에서 만나는 조건 약간 놓친듯
     else:print(0)

