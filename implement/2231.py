n = int(input())
for i in range(1,n+1):
    check = i
    memo = i
    while i > 0:
        check += i%10
        i //= 10
    if(check == n):
        print(memo)
        n = 0
        break
if n != 0: print(0)
