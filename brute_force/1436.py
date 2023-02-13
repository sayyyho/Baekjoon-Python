import sys

n = int(input())
check = 0

for i in range(666, sys.maxsize):
    if "666" in str(i):
        check += 1
    if n == check: 
        print(i)
        break