def find_prime(i):
    if i < 2:
        return 0
    k = 2
    while (k < i):
        if (i % k == 0):
            return 0
        k +=1
    return 1

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    cnt += find_prime(i)
print(cnt)