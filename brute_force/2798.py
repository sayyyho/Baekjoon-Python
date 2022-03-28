# study brute force

n, target = map(int , input().split())
data = list(map(int , input().split()))
res = 0

for i in data:
    for j in data:
        for k in data:
            if (i != j) and (j != k) and k != i:
                if (target - res > target - (i+j+k) and target - (i+j+k) > -1):
                    res = i+j+k
print(res)