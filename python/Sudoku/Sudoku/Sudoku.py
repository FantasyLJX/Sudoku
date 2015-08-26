#进度：使用唯一求解法解简单数独，或求出复杂数独的候选数

#创建候选数列表
solution = [[[1,2,3,4,5,6,7,8,9] for i in range(9)] for j in range(9)]

#暂存已确定数的【行、列、数值】
defined = []

#输入数独题目,并用于存放计算结果
sudoku = []
print("请输入数独题目，未知数用0代替，每个数字以逗号隔开：")
for i in range(9):
    sudoku.append(list(eval(input("第" + str(i+1) + "行:"))))

#测试数独题库
#sudoku = [[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]]
#sudoku = [[0,4,0,2,5,0,0,0,8],[0,3,0,4,0,9,1,7,0],[0,0,0,0,8,1,2,0,0],[0,0,6,0,0,0,7,2,0],[0,0,0,6,0,4,0,0,0],[0,1,2,0,0,0,3,0,0],[0,0,3,8,1,0,0,0,0],[0,6,4,9,0,2,0,1,0],[7,0,0,0,4,5,0,9,0]]


#移除row行col列中的候选数num
def ReMove(row,col,num):
    if(num in solution[row][col]):
        solution[row][col].remove(num)
        if(len(solution[row][col]) == 1):
            defined.append([row,col,solution[row][col][0]])
            sudoku[row][col] = solution[row][col][0]
#根据已确定数，删除候选数列表【行、列、宫】中的相同数
def Delete(row,col,num):
    for i in range(9):
        if(i != row):
            ReMove(i,col,num)
    for i in range(9):
        if(i != col):
            ReMove(row,i,num)
    row_h = int(row / 3) * 3
    col_h = int(col / 3) * 3
    for i in range(row_h,row_h + 3):
        for j in range(col_h,col_h + 3):
            if(i != row and j != col):
                ReMove(i,j,num)

#唯一求解法
def Unique():
    while(len(defined) != 0):
        temp = defined.pop()
        Delete(temp[0],temp[1],temp[2])


for i in range(9):
    for j in range(9):
        if(sudoku[i][j] != 0):
            defined.append([i,j,sudoku[i][j]])
            solution[i][j] = [sudoku[i][j]]

Unique()

print("已解出数：")
for i in range(9):
    print(sudoku[i])

print("候选数列表：")
for i in range(9):
    print(solution[i])
