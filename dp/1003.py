case_box = []
start = 2
n = int(input())
for _ in range(0,n):
    case_box.append(int(input()))
for end in case_box:
    data = []
    data.append([1,0])
    data.append([0,1])
    for i in range(start, end+1):
        data.append([data[i-1][0] + data[i-2][0] , data[i-1][1] + data[i-2][1]])
    print(data[end][0], end=' ') 
    print(data[end][1])