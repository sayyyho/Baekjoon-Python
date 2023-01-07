n = int(input())

for _ in range(n):
    datas = list(input())
    check = 0
    score = 0
    for data in datas:
        if(data=="O"):check+=1
        else:check=0
        score+=check
    print(score)