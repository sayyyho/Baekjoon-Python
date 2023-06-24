while True:
    string = input()
    if string == ".": break
    strings = list(string)
    count1 = 0
    count2 = 0
    data = []
    for string in strings:
        print(string)
        if string == ".":
            break
        if string == '(':
            count1 += 1
            data.append(0)
        elif string == "[":
            count2 += 1
            data.append(1)
        elif string == ")":
            count1 -= 1
            if count1 < 0:
                print("no")
                break
            if data[-1] == 0:
                data.pop()
                count1+=1
            else:
                print("no")
                break
        elif string == "]":
            count2 -= 1
            if count2 < 0:
                print("no")
                break
            if data[-1] == 1:
                count2 += 1
                data.pop()
            else:
                print("no")
                break            
        else:
            continue
        print(1)
    if count1 == 0 and count2 == 0:
        print("yes")