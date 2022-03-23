n = int(input())
length = 0
arr = []
while (n > 0):
    arr.append(n%10)
    n //= 10
    length +=1
arr.sort(reverse=True)
for i in range(length):
    print(arr[i], end='')