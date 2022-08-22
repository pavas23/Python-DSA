# Given two integers M & N, calculate and return their multiplication using recursion. You can only use subtraction and addition for your calculation. No other operators are allowed.
# Input format :
# Line 1 : Integer M
# Line 2 : Integer N
# Output format :
# M x N
# Constraints :
# 0 <= M <= 1000
# 0 <= N <= 1000
# Sample Input 1 :
# 3 
# 5
# Sample Output 1 :
# 15
# Sample Input 2 :
# 4 
# 0
# Sample Output 2 :
# 0

## Read input as specified in the question.
## Print output as specified in the question.
from sys import setrecursionlimit
setrecursionlimit(10**6) 


def multi(n,m):
    if n==0 or m==0:
        return 0
    smalloutput = multi(n,m-1)
    return n + smalloutput
    
       
n = int(input())
m = int(input())
x = multi(n,m)
print(x)
