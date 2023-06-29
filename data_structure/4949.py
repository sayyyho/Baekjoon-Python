while True:
    stack = list()
    flag = 0
    string = input()
    if string == ".": break
    for c in string:
        if c == "(": stack.append(c)
        elif c == "[": stack.append(c)
        elif c ==")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = 1
                break
        elif c =="]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = 1
                break    
    if flag == 1 or stack: print("no")
    else: print("yes")       