while True:
    n = int(input())
    if n == 0: break
    data = list(str(n))
    length = len(data)
    for i in range(0, len(data)//2 + 1):
        if data[i] == data[length - 1]:
            length -= 1
        else:
            print("no")
            length = -1
            break
    if length != -1: print("yes")