flag1 = 1
flag2 = 0

def fib(n):
    global flag1
    if (n == 1 or n == 2):
        return 1
    else: 
        flag1+=1
        return (fib(n - 1) + fib(n - 2))

def fibonacci(n):
    global flag2
    f[1] = 1 
    f[2] = 1
    for i in range (3, n+1):
        f[i] = f[i - 1] + f[i - 2]
        flag2 += 1
    return f[n]


n = int(input())
f = [0 for _ in range(n+1)]
result1 = fib(n)
result2 = fibonacci(n)
print(flag1, flag2)
# print(result1, result2)