# Given an array consisting of positive and negative integers, find the length of the longest subarray whose sum is zero.
# Input Format:
# The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
# The following line contains N space separated integers, that denote the value of the elements of the array.
# Output Format
# The first and only line of output contains length of the longest subarray whose sum is zero.
# Constraints:
# 0 <= N <= 10^8
# Time Limit: 1 sec

def subsetSum(l):
    d = {}
    maxsum = float("-inf")
    sum = 0
    
    i=0
    for ele in l:
        sum += ele
        if sum == 0:
            maxsum = max(i+1, maxsum)
            
        if sum in d:
            count = i - d[sum]
            maxsum = max(count, maxsum)
        
        d[sum] = i
        i += 1
            
    return maxsum
    
    
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))
