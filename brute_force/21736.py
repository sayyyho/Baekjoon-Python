n, m = map(int, input().split())

campus_map = list()

for _ in range(n): campus_map.append(list(input()))

count = 0

for row in range(n):
    for col in range(m):
        if campus_map[row][col] == "O" or campus_map[row][col] == "I":
            if row < n - 2 and campus_map[row + 1][col] == "P" :
                    count += 1
                    campus_map[row + 1][col] = "O"
            if row > 0 and campus_map[row - 1][col] == "P":
                    count += 1
                    campus_map[row - 1][col] = "O"
            if col < m - 2 and campus_map[row][col + 1] == "P":
                    count += 1
                    campus_map[row][col + 1] = "O"
            if col > 0 and campus_map[row][col - 1] == "P":
                    count += 1
                    campus_map[row][col - 1] = "O"
                    
if count == 0: print("TT")
else: print(count)