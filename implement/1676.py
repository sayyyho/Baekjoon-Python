n = int(input())
import math

result = math.factorial(n)

datas = list(str(result))
datas.reverse()

cnt = 0

for data in datas:
    if data == "0": cnt +=1
    else: break
print(cnt)