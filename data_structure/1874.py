n = int(input())

goal = []
now = []
func = []

for _ in range(n):
    goal.append(int(input()))

index = 0
check = 1

while index < n:
    flag = 0
    while True:
        if len(now) >= 1 and goal[index] == now[-1]:
            func.append("-")
            now.pop()
            flag = 1
            break
        if goal[index] >= check:
            func.append("+")
            now.append(check)
            check+=1
        elif len(now)>=1 and goal[index] < check:
            func.append("-")
            now.pop()
        if len(now) == 0: break
    index+=1
    if flag == 0: 
        print("NO")
        break
if flag == 1:
    print(*func, sep="\n")