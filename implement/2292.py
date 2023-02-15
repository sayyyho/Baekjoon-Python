n = int(input())

val = 1
cnt = 0

while True:
    if n - val < 1:
        print(cnt+1)
        break
    cnt+=1
    val = val + cnt*6