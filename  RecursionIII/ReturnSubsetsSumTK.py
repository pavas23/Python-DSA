# Given an array A of size n and an integer K, return all subsets of A which sum to K.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Note : The order of subsets are not important.
# Input format :
# Line 1 : Integer n, Size of input array
# Line 2 : Array elements separated by space
# Line 3 : K 
# Constraints :
# 1 <= n <= 20
# Sample Input :
# 9 
# 5 12 3 17 1 18 15 3 17 
# 6
# Sample Output :
# 3 3
# 5 1

import sys
sys.setrecursionlimit(10**6)

def subsetsSumKHelper(arr, startIndex, k) :
    if startIndex == len(arr) :
        if k == 0 :
            return [list()]
        else :
            return list()
        
    smallOutput1 = subsetsSumKHelper(arr, startIndex + 1, k) 
    smallOutput2 = subsetsSumKHelper(arr, startIndex + 1, k - arr[startIndex]) 
    
    output = (len(smallOutput1) + len(smallOutput2)) * [0]
    
    index = 0
    for i in range(len(smallOutput1)) :
        output[index] = smallOutput1[i]
        index += 1
        
    for i in range(len(smallOutput2)) :
        output[index] = (len(smallOutput2[i]) + 1) * [0]
        output[index][0]= arr[startIndex]
        
        for j in range(len(smallOutput2[i])) :
            output[index][j+1] = smallOutput2[i][j]
            
        index += 1
        
    return output
        

def subsetsSumK(arr, k) :
    return subsetsSumKHelper(arr, 0, k)

#taking input
def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


#printing the list of lists
def printListOfList(liOfLi) :
    for li in liOfLi :
        for elem in li :
            print(elem, end = " ")
        print()

#main
arr, n = takeInput()

if n != 0 :
    k = int(input().strip())
    liOfLi = subsetsSumK(arr, k)
    printListOfList(liOfLi)
