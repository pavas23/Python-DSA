# Given an integer array (of length n), find and print all the subsets of input array.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Note : The order of subsets are not important. Just print the subsets in different lines.
# Input format :
# Line 1 : Integer n, Size of array
# Line 2 : Array elements (separated by space)
# Constraints :
# 1 <= n <= 15
# Sample Input:
# 3
# 15 20 12
# Sample Output:
# [] (this just represents an empty array, don't worry about the square brackets)
# 12 
# 20 
# 20 12 
# 15 
# 15 12 
# 15 20 
# 15 20 12 

import sys
sys.setrecursionlimit(10**6)


def printSubHelper(arr,output,si):
    n = len(arr)
    if si == n:
        for i in range(len(output)):
            print(output[i],end=" ")
        print()
        return
    
    new_arr = []
    for i in range(len(output)):
        new_arr.append(output[i])
        
    new_arr.append(arr[si])
    printSubHelper(arr,new_arr,si+1)
    printSubHelper(arr,output,si+1)



def printSub(arr):
    si = 0
    output = []
    printSubHelper(arr,output,si)


  
n=int(input())
arr = [int(element) for element in list(input().strip().split(" "))]
printSub(arr)
