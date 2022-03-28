data = [0] * 43
res = 0

for _ in range(10):
    number = int(input())
    data[number % 42] += 1

for i in data:
    if (i > 0):
        res +=1
print(res)