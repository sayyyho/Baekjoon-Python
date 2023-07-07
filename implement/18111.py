n, m, b = map(int, input().split())

def check_valid(needs):
    global b
    if abs(needs) > b:
        return False
    b += needs
    return True

num = [0] * 257

datas = list()

for _ in range(n):
    for value in list(map(int, input().split())): 
        num[value] +=1
        datas.append(value)
freq = [i for i, ele in enumerate(num) if ele == max(num)]
max_freq = max(freq)
new = [data - max_freq for data in datas]
result = 0

flag = 0

for check in new:
    if check < 0: 
        valid = check_valid(check)
        if valid == False: 
            flag = 1
            break
        else:
            result += abs(check)
    else: result += 2 * check
if flag == 1:
    max_freq -= 1
    for check in new:
            result += 2 * (check + 1 )

print(result, max_freq)


import sys
n, m, b = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height = 0
ans = 1000000000000000000000000000000
for i in range(257):
    max = 0
    min = 0
    for j in range(n):
        for k in range(m):
            if table[j][k] < i:
                min += (i - table[j][k])
            else:
                max += (table[j][k] - i)
    inventory = max + b
    if inventory < min:
        continue
    time = 2 * max + min
    if time <= ans:
    # 시간이 같을 때는 높이가 높은 순으로 출력하라는 조건에 맞게
    # for i in range(257)은 항상 i가 오름차순으로 돌기 때문에
    # 시간이 같아도 최종적으로는 높이가 높은 순으로 나오게 된다
        ans = time
        height = i
print(ans, height)