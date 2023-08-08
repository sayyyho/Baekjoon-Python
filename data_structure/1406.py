import sys; input = sys.stdin.readline
left_stack = list(input().rstrip())
right_stack = list()

for _ in range(int(input())):
    data = input()
    if data[0] == "P":
        left_stack.append(data[2])
    if data[0] == "L":
        if left_stack: right_stack.append(left_stack.pop())
    if data[0] == "D":
        if right_stack: left_stack.append(right_stack.pop())
    if data[0] == "B":
        if left_stack: left_stack.pop()
result = left_stack + right_stack[::-1]        
print(*result, sep="")