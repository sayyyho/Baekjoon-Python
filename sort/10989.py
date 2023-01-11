import sys

n = int(input())

memos = [0] * 10001
for _ in range(n):memos[int(sys.stdin.readline())] += 1
for i in range(1, 10001):
    while(memos[i]):
        sys.stdout.write(str(i) + '\n')
        memos[i] -=1