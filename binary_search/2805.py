n, goal = map(int, input().split())
datas = list(map(int, input().split()))

def binary_search(low, high): #절단기 길이에 대한 이분탐색 -> 목표 나무길이에 근사하는(같으면 베스트) 절단기 길이 최대값이 목표 -> 기준은 mid다. mid로 자르는중
    if low > high:
        print(high)
        return
    mid = (low + high) // 2
    length = 0 #나무 길이
    for data in datas:
        if data - mid > 0: length += (data - mid)
    if length >= goal: binary_search(mid+1, high)
    else: return binary_search(low, mid-1)

binary_search(1, max(datas))