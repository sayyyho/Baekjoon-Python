n = int(input())
data = list(map(int, input().split()))
data.sort()
if (n % 2 == 0):
    print(data[0] * data[n-1])
else:
    print(data[n//2]**2)
