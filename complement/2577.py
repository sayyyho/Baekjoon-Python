import sys
datas = list()
for i in range(3):
    datas.append(int(sys.stdin.readline()))
m = datas[0] * datas[1] * datas[2]
datas = [0]*10
idx = 1
check = 10
while (True):
    if(m-check < 0):break
    idx +=1
    check *=10
check //= 10
while(check > 0):
    k =m // check
    datas[k] +=1
    m%=check
    check //= 10
for data in datas:
    print(data)
