data = []
data.append((input()))

length = len(data[0])

for i in range(1, length):
    string = ""
    for j in range(i, length):
        string += data[0][j]
    data.append(string)

data.sort()
print(*data , sep="\n")

# S = input()
# suffixes_list = sorted([S[i:] for i in range(len(S))])
# for i in suffixes_list:
#     print(i)