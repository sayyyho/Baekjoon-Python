
def print_form(n, case, row, col):
    flag = 0
    if (((row >= case)and(row < case * 2))and((col >= case)and(col < case * 2))):
        print(" ", end ='')
        col += 1
        flag = 1
    
    elif(case != 1):
        print_form(n, case //3, row, col)
    if (case != n // 3):
        return
    if (flag == 0 and case == n // 3):
        print("*", end ='')
        col +=1
    if (col == n):
        col = 0
        row += 1
        print("")
    if (n == row):
        return
    print_form(n, case, row, col)


n = int(input())
print_form(n, n//3, 0, 0)