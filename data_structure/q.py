from collections import deque
queue = deque()

while(True):
    op = input("input operation : ")
    if op == "push": queue.append(input("input value : "))
    elif op == "pop": queue.popleft()
    else: break

print(queue)
print(list(queue))
queue.reverse()
print(queue)