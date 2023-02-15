n = int(input())

for _ in range(n):
    datas = list(input())
    cnt = 0
    for data in datas:
        if data == '(': cnt+=1
        if data == ')': cnt-=1
        if cnt < 0: break
    if cnt == 0: print('YES')
    else: print("NO")