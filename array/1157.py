word = list(input())
ord_word = []
for alph in word:
    if(ord(alph)>90):ord_word.append(ord(alph)-32)
    else:ord_word.append(ord(alph))
ord_word.sort()
max = -1
idx = -1
for num in range(65, 91):
    check = 0
    for alph in ord_word:
        if(num == alph):
            check += 1

    if(check==max):
        idx = "?"
    if(check > max):
        max = check
        idx = num

if(idx=="?"):print(idx)
else:print(chr(idx))
