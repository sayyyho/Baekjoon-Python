n = int(input())
r = 31
M = 1234567891
value = list(input())
result = 0
for i in range(n):
    result += (ord(value[i]) - 96) * pow(r,i)  

result %= M
print(result)  
