import sys
n = int(sys.stdin.readline())

data = list()

for _ in range(n):
    data.append(int(sys.stdin.readline()))    
    
data.sort()
value = int(n*0.15 + 0.5)
result = 0

for i in range(value, n - value):
    result += data[i]
    
divisor = n - 2 * value
if divisor == 0: print(0)
else:print(int(result / divisor  + 0.5))