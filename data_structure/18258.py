from collections import deque
import sys

n = int(input())

queue = deque()

for _ in range(n):
    data = sys.stdin.readline()
    data = data.split()
    if data[0] == 'push':queue.append(data[1])
    elif data[0] == 'pop':
        try:
            print(queue[0])
            queue.popleft()
        except:
            print(-1)
    elif data[0] == 'size': print(len(queue))
    elif data[0] == 'empty': 
        if len(queue) == 0: print(1)
        else: print(0)
    elif data[0] == 'front':
        try:print(queue[0])
        except: print(-1)
    elif data[0] == 'back':
        try:print(queue[-1])
        except:print(-1)