import math
a,b,v = map(int, input().split(" "))
print(math.ceil((v - a) / (a-b)) + 1) # v-a로 최종 점프 전 날까지 움직이고, (a-b)로 여기까지 며칠 걸렸는지 체크 후 하루 더 해 주면 정상 도달 일.