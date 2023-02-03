n = int(input())
time_info = [list(map(int, input().split())) for _ in range(n)]
sorted_time = sorted(time_info, key=lambda data: (data[1], data[0]))
end = 0
cnt = 0

for i in range(0, n):
    if sorted_time[i][0] >= end:
        end = sorted_time[i][1]
        cnt += 1

print(cnt)