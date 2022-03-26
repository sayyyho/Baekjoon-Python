data = []
idx = 0
max = 0
for i in range(9):
    data.append(int(input()))
    if (max < data[i]):
        max = data[i]
        idx = i + 1
print(max)
print(idx)