n, c = map(int, input().split())

datas = []

for _ in range(n): datas.append(int(input()))

def binary_search(low, high):
    mid = (low + (high - low) // 2)
    sum = 0
    for data in datas: sum += data // mid
    if low > high: #low값을 계속 올려서 high값보다 크면, high값은 안되는 범위에서 내린걸텐데 즉 high값이 max 
        print(high) #최대 랜선을 보여줘야 해서 high 출력
        return
    if sum >= n: # 더 확인해봐야하는 경우 : 이 지점을 low checking point로 잡고... return 때리기.
        return binary_search(mid+1, high) #2 크거나 같은 경우 low 값을 올리는데
    else: # 아예 mid를 내려야하는 경우  
        return binary_search(low, mid-1) #1 작은경우 high값을 내리고


datas.sort()

target = (max(datas) - min(datas)) // 2
start = min(datas)
for _ in range(c):
    binary_search(start, target)
    start = start + 3
    
        


