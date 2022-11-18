n = int(input())
for i in range(1,n+1):
    for _ in range(i, n):print(" ",end="")
    for _ in range(0, i):print("*",end="")
    print()