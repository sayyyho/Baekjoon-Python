n, m = map(int, input().split())
data = [list(input()) for _ in range(n)]
result_box = []

row_trial = n - 7
col_trial = m - 7 # 기본 8이면 1번 check 가능
row_check = 0


#brute_force 구현부

while(row_trial > row_check):
    col_check = 0
    while(col_trial > col_check):
        white_count = 0
        black_count = 0
        count = 0
        white = "W"
        black = "B"
        for i in range(row_check, 8+row_check): #행 8번 탐색
            for j in range(col_check, 8+col_check): #열 8번 탐색
                if (row_check %2 ==0):
                    if (i%2==0): 
                        if(j%2==0): 
                            if(data[i][j] != white):white_count+=1
                            if(data[i][j] != black):black_count+=1
                        else:
                            if(data[i][j] == white):white_count+=1
                            if(data[i][j] == black):black_count+=1
                    else:
                        if(j%2==0):
                            if(data[i][j] == white):white_count+=1
                            if(data[i][j] == black):black_count+=1
                        else:
                            if(data[i][j] != white):white_count+=1
                            if(data[i][j] != black):black_count+=1
                else:
                    if (i%2==1): 
                        if(j%2==1): 
                            if(data[i][j] != white):white_count+=1
                            if(data[i][j] != black):black_count+=1
                        else:
                            if(data[i][j] == white):white_count+=1
                            if(data[i][j] == black):black_count+=1
                    else:
                        if(j%2==0):
                            if(data[i][j] != white):white_count+=1
                            if(data[i][j] != black):black_count+=1
                        else:
                            if(data[i][j] == white):white_count+=1
                            if(data[i][j] == black):black_count+=1
        count = min(white_count, black_count)
        col_check+=1
        result_box.append(count)
        if(white_count>0):result_box.append(white_count)
    row_check+=1
print(min(result_box)) 