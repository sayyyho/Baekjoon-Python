import sys

n = int(input())
stack = []
index = -1
for _ in range(n):
    op = sys.stdin.readline().split()
    if(op[0]=='push'):
        stack.append(op[1])
        index += 1
    elif(op[0]=='top'):
        if(index > -1):
            print(stack[index])
        else:
            print(-1)
    elif(op[0]=='empty'):
        if(index < 0):
            print(1)
        else:
            print(0)
    elif(op[0]=='size'):
        if(index < 0):
            print(0)
        else:
            print(index+1)
    elif(op[0]=='pop'):
        if(index > -1):
            print(stack[index])
            stack.pop()
            index -= 1
        else:
            print(-1)

