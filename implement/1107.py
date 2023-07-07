import sys
input = sys.stdin.readline
target = int(input())
broken = int(input())
broken_button = list(map(int,input().split()))

result = abs(target - 100)

for i in range(1000001):
    check = str(i)
    for index in range(len(check)):
        if int(check[index]) in broken_button:
            break
        elif index == len(check) - 1:
            result = min(result, abs(int(check) - target) + len(check))
print(result)
