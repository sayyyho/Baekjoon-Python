import sys; input = sys.stdin.readline
import heapq

n = int(input())
ctr_data = {}

for _ in range(n):
    number = int(input())
    if number in ctr_data.keys():
        ctr_data[number] = ctr_data[number] + 1
    else:
        ctr_data[number] = 1

target = max(ctr_data.values())
heap = []

for key, value in ctr_data.items():
    if value == target:
        heapq.heappush(heap, key)
print(heap[0])

# n = int(input())
# dic = {}

# for case in range(n):
#     tmp = int(input())
#     if tmp in dic:
#         dic[tmp] += 1
#     else:
#         dic[tmp] = 1

# dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
# print(dic[0][0])