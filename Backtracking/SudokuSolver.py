def isValid(board,row,col,po):
    # checking for a row
    for j in range(9):
        if board[row][j] == po:
            return False
    # checking for a col
    for i in range(9):
        if board[i][col] == po:
            return False
    # checking for a submatrix
    smi = int(row/3)*3
    smj = int(col/3)*3
    for i in range(3):
        for j in range(3):
            if board[smi+i][smj+j] == po:
                return False         
    return True

def solveSudoku(board,i,j):
    if i == 9:
        # for i in range(9):
        #     for j in range(9):
        #         print(board[i][j],end=" ")
        #     print()
        return True
    # increasing i and j
    if j == 8:
        ni = i + 1
        nj = 0
    else:
        ni = i
        nj = j + 1
        
    if board[i][j] != 0:
        return solveSudoku(board,ni,nj)
    else:
        for po in range(1,10,1):
            if isValid(board,i,j,po):
                board[i][j] = po
                if solveSudoku(board,ni,nj) is True:
                    return True
                else:
                    board[i][j] = 0
    # if no num is possible to fill
    return False

board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board,0,0)
if ans is True:
    print('true')
else:
    print('false')

    