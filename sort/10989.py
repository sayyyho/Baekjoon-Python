import sys

n = int(input())
count_arr = [0] * 10001

for _ in range(n):
    number = int(sys.stdin.readline())
    count_arr[number] +=1

for index in range(10001):
    while(count_arr[index] > 0):
        print(index)
        count_arr[index] -= 1
