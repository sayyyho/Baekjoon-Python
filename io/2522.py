n = int(input())

i = 1
flag = 0
while True:
    if flag == 0: 
        print(" "*(n-i),end="")
        print("*"*(i))
        i +=1
    else:
        i -=1
        print(" "*(n-i),end="")
        print("*"*(i))
    if i > n: 
        flag = 1
        i -= 1
    if flag == 1 and i == 1: break    
    
    
    