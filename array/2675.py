n = int(input())
for _ in range(n):
    num , str = input().split()
    datas = list(str)
    num = int(num)
    for data in datas:
        print(data*num,end="")
    print()