from collections import deque

n = int(input())

for _ in range(n):
    index , target = map(int, input().split())
    data = list(map(int, input().split()))
    i_data = [i for i in range(index)]
    queue = deque(data)
    i_queue = deque(i_data)
    cnt = 0
    while True:
        if queue[0] == max(queue):
            queue.popleft()
            cnt+=1
            if i_queue[0] == target:
                print(cnt)
                break
            else: i_queue.popleft()
        else:
            queue.append(queue.popleft())
            i_queue.append(i_queue.popleft())