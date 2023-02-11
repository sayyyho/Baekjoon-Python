n, k = map(int, input().split())
member = [i for i in range(0, n+1)]
check = k

print("<", end="")

while True:
    print(member[check], end="")    
    member[check] = 0
    if sum(member) == 0: break
    print(",", end=" ")
    count = 0
    while True:
        check+=1
        if check == len(member): check = 1
        if member[check] != 0: count+=1
        if count == k:break
        
print(">")