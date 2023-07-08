x , y = map(int, input().split())
list_31 = [1,3,5,7,8,10,12]
list_30 = [4,6,9,11]
day_list = ["SUN", "MON", "TUE" ,"WED", "THU", "FRI","SAT"]

check = 0

for i in range(1,x):
    if i in list_31: check +=31
    elif i in list_30: check +=30
    else: check += 28
check += y
print(day_list[check%7])