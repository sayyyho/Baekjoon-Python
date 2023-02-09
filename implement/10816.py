import sys
input = sys.stdin.readline

# def binary_search(low, high, card, count):
#     mid = low + (high - low) // 2
#     if low > high: 
#         return count
#     if base[mid] == card:
#         count += 1
#         base.pop(mid)
#         high = i - 1 - count                                 
#     elif base[mid] > card: high = mid - 1
#     else: low = mid + 1
#     return binary_search(low, high, card, count)

_ = int(input()) # _ 미사용 값
base = list(map(int, input().split()))
base.sort()
_ = input()
cards = list(map(int, input().split()))
data = {}

for value in base:
    if value in data: data[value] += 1
    else: data[value] = 1

for card in cards:
    if card in data: print(data[card], end=" ")
    else: print(0, end=" ")

# for card in cards:
#     count = binary_search(0, i-1, card, 0)
#     i -= count
#     data.append(count)



# from sys import stdin
# from collections import Counter
# _ = stdin.readline()
# N = stdin.readline().split()
# _ = stdin.readline()
# M = stdin.readline().split()

# C = Counter(N)
# print(' '.join(f'{C[m]}' if m in C else '0' for m in M))