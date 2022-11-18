numlist = list(map(int, input().split()))
acc = 0
for i in numlist:
    acc += i**2
print(acc%10)