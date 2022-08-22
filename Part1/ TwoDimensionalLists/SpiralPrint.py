# For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. That is, you need to print in the order followed for every iteration:
# a. First row(left to right)
# b. Last column(top to bottom)
# c. Last row(right to left)
# d. First column(bottom to top)
#  Mind that every element will be printed only once.
# Refer to the Image:
# Spiral path of a matrix

# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

# Second line onwards, the next 'N' lines or rows represent the ith row values.

# Each of the ith row constitutes 'M' column values separated by a single space.
# Output format :
# For each test case, print the elements of the two-dimensional array/list in the spiral form in a single line, separated by a single space.

# Output for every test case will be printed in a seperate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^3
# 0 <= M <= 10^3
# Time Limit: 1sec
# Sample Input 1:
# 1
# 4 4 
# 1 2 3 4 
# 5 6 7 8 
# 9 10 11 12 
# 13 14 15 16
# Sample Output 1:
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
# Sample Input 2:
# 2
# 3 3 
# 1 2 3 
# 4 5 6 
# 7 8 9
# 3 1
# 10
# 20
# 30
# Sample Output 2:
# 1 2 3 6 9 8 7 4 5 
# 10 20 30 

from sys import stdin



def spiralPrint(mat, nRows, mCols):
    if nRows==0 or mCols==0 :
        return
    
    left,right = 0,mCols
    up,down = 0,nRows
    count=0
    ii,jj,total=left,up,(nRows*mCols)
    
    while True:
        for i in range(left,right):
            print(mat[jj][i] , end=" ")
            ii=i
            count+=1
            if count==total:
                return
        up+=1

        for j in range(up,down):
            print(mat[j][ii] , end=" ")
            jj=j
            count+=1
            if count==total:
                return
        right-=1

        for i in range(right-1,left-1,-1):
            print(mat[jj][i] , end=" ")
            ii=i
            count+=1
            if count==total:
                return
        down-=1

        for j in range(down-1,up-1,-1):
            print(mat[j][ii] , end=" ")
            jj=j
            count+=1
            if count==total:
                return
        left+=1




# def spiralPrint(mat, nRows, mCols):
#     #Your code goes here
#     str1 = ''
#     x = 0
#     count = 0
#     a,b = 0,0
#     i,j= 0,0
#     if nRows ==0 and mCols ==0:
#         print()
#     else:
#         while(count <= nRows*mCols):
#             # row wise iteration ( left to right)
#             for i in range(0+a,nRows,1):
#                 for j in range(0+b+i,mCols,1):
#                     str1 += str(mat[i][j])
#                     str1 += " "
#                     count += 1
#                 break
#             # col wise iteration ( top to bottom)
#             for j in range(mCols-1,-1,-1):
#                 for i in range(i+1,nRows,1):
#                     str1 += str(mat[i][j])
#                     str1 += " "
#                     count += 1
#                 break    
#             # row wise iteration (right to left)
#             for i in range(nRows-1,-1,-1):
#                 for j in range(j-1,-1,-1):
#                     str1 += str(mat[i][j])
#                     str1 += " "
#                     count += 1
#                 break
#             # col wise iteration (bottom to top)
#             for j in range(0,mCols,1):
#                 for i in range(i-1,nRows-i-3,-1):
#                     str1 += str(mat[i][j])
#                     str1 += " "
#                     count += 1
#                 break  
#             a = i
#             b = j
#         print(str1)
    
    

#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1