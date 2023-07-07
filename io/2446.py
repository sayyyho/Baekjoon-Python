n = int(input())
i = 0
while (n > 0):
    if i != 0:
        print()
    print(" "*i ,end="")
    print("*"*(2*n -1),end="")
    
    i += 1
    n -= 1
i-=2
n+=2
while (i > -1):
    print()
    print(" "*i ,end="")
    print("*"*(2*n -1),end="")
    i -= 1
    n +=1
