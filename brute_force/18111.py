n, m, b = map(int, input().split())

datas = list()
height_count = [0] * 257
optimization = 500*500*2*257
final_height = 0

for _ in range(n):
    data = list(map(int, input().split()))
    for i in data: 
        height_count[i] +=1
        datas.append(i)

for check in range(257):
    incomming = 0
    outgoing = 0
    for data in datas:
        if data > check: incomming += data - check
        else: outgoing += check - data
    if b + incomming < outgoing:
        continue        
    cost = 2 * incomming + outgoing
    if cost <= optimization: 
        optimization = cost
        final_height = check 
               
print(optimization, final_height)
                            