num, total = map(int, input().split())
datas = []
for _ in range(num):datas.append(int(input()))
datas.sort(reverse=True)

def greedy(total):
    cnt = 0
    while True:
        for data in datas:
            if total - data < 0:continue
            total -= data
            cnt += 1
            break
        if total <= 0:break
    print(cnt)
greedy(total)