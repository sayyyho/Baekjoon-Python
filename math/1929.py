import math

n, m = map(int, input().split())

def isPrime(i):
    if(i==2 or i==3):
        print(i)
        return
    if (i % math.sqrt(i) == 0):return
    for k in range(2,int(math.sqrt(i))+1):
        if (i % k == 0):return
    print(i)
    return
for i in range(n,m+1):
    if(i==1):continue
    else:isPrime(i)

