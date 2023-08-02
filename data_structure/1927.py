import heapq
import sys; input = sys.stdin.readline

heap = []
n = int(input())

for _ in range(n):
    op = int(input())
    if op == 0:
        if not heap: print(0)
        else: print(heapq.heappop(heap))
    else: heapq.heappush(heap, op)
