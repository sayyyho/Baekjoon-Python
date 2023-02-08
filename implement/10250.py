import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    H, W, P = map(int, input().split())
    floor = P % H
    num = P // H + 1
    if floor == 0: 
        floor = H
        num -=1 
    if num < 10: print(str(floor) + "0" + str(num))
    else: print(str(floor) +  str(num))

    # print(f'{floor*100+num}') // f 표현식