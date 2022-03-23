def mulNmod(a, b, c):
    if (b == 1):
        return a % c
    if (b % 2 == 0):
        res = mulNmod(a, b//2, c)
        return (res * res) % c
    else:
        res = mulNmod(a, (b-1)//2, c)
        return (res * res * a) % c

a, b, c = map(int, input().split())
print(mulNmod(a, b, c))
