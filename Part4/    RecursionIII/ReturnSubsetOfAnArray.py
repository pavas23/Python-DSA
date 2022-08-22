# Given an integer array (of length n), find and return all the subsets of input array.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Note : The order of subsets are not important.
# Input format :

# Line 1 : Size of array

# Line 2 : Array elements (separated by space)

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


def subset(nums):
    if len(nums)==0:
        op = [[]]
        return op

    ele = nums[-1:]
    arr = subset(nums[:-1])
    ans = []

    for i in arr:
        ans.append(i)

    for i in arr:
        ans.append(i+ele)

    return ans

    
n=int(input())
arr = [int(element) for element in list(input().strip().split(" "))]
output=subset(arr)
for i in output:
    for j in i:
        print(j,end=" ")
    print()