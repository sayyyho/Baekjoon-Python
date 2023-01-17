stack = []

while(True):
    op = input("input operation : ")
    if op == "push": stack.append(input("input value : "))
    elif op == "pop": stack.pop()
    else: break

print(stack)
print(stack[::-1])