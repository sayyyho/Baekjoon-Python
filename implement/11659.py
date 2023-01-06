import sys
num, count = map(int, input().split())
num_list = list(map(int, sys.stdin.readline().split()))
sum_list = [0 for _ in range(num+1)]
for i in range(num):
    sum_list[i+1] = sum_list[i] + num_list[i]

for _ in range(count):
    s, e = map(int, sys.stdin.readline().split())
    print(sum_list[e] - sum_list[s-1])