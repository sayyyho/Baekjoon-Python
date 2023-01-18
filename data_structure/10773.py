import sys

n = int(input())
stack = []

for _ in range(n):
    value = int(sys.stdin.readline())
    if value == 0: stack.pop()
    else: stack.append(value)
print(sum(stack))