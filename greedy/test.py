import math

x, y = map(int, input().split())
z = math.trunc((y/x) * 100)
cnt = 0

if x==y:cnt=-1
else:
    while True:
        x+=1
        y+=1
        cnt+=1
        if z != math.trunc((y/x)*100): break
        z = math.trunc((y/x) * 100)
         
print(cnt)