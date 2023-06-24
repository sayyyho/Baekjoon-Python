# import math
# # n개를 만족하는 동일 최대길이 랜선의 세트

# x, y = map(int, input().split())
# z = math.trunc((x/y) * 100)

# def binary_search(high, low):
#     mid = (low + (high - low) // 2)
#     sum = 0
#     for data in datas: sum += data // mid
#     if low > high: #low값을 계속 올려서 high값보다 크면, high값은 안되는 범위에서 내린걸텐데 즉 high값이 max 
#         print(low) #최소 변경점을 보여줘야 해서 low 출력
#         return
#     if sum >= z: # 더 확인해봐야하는 경우 : 이 지점을 low checking point로 잡고... return 때리기.
#         return binary_search(mid+1, high) #2 크거나 같은 경우 low 값을 올리는데
#     else: # 아예 mid를 내려야하는 경우  
#         return binary_search(low, mid-1) #1 작은경우 high값을 내리고

# if x == y:print(-1)

# else:binary_search(x,y)

# #미드로 체크하면서 최대 범위까지 탐색
