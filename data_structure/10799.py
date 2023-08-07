import sys; input = sys.stdin.readline

data = input()
stack = []
cnt = 0
result = 0

for value in data:
    if not stack: 
        if value == "(": cnt += 1
        stack.append(value)
        flag = 0
    else:
        if flag == 0 and stack[-1] == "(" and value == ")":
            flag = 1
            stack.pop()
            cnt -= 1
            if cnt > 0: result += cnt
        else:
            if value == ")": 
                flag = 1
                result += 1
                cnt -= 1
                stack.pop()
            else: 
                flag = 0
                stack.append(value)
                cnt += 1
print(result)