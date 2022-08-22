# You are given an integer array/list(ARR) of size N. It contains only 0s, 1s and 2s. Write a solution to sort this array/list in a 'single scan'.
# 'Single Scan' refers to iterating over the array/list just once or to put it in other words, you will be visiting each element in the array/list just once.
# Note:
# You need to change in the given array/list itself. Hence, no need to return or print anything. 
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First line of each test case or query contains an integer 'N' representing the size of the array/list.

# Second line contains 'N' single space separated integers(all 0s, 1s and 2s) representing the elements in the array/list.
# Output Format :
# For each test case, print the sorted array/list elements in a row separated by a single space.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^5
# Time Limit: 1 sec
# Sample Input 1:
# 1
# 7
# 0 1 2 0 2 0 1
# Sample Output 1:
# 0 0 0 1 1 2 2 
# Sample Input 2:
# 2
# 5
# 2 2 0 1 1
# 7
# 0 1 2 0 1 2 0
# Sample Output 2:
# 0 1 1 2 2 
# 0 0 0 1 1 2 2

from sys import stdin 

def sort012(arr, n) :
    #Your code goes here
    lo = 0
    hi = n - 1
    mid = 0
    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo = lo + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi = hi - 1
    return arr

    
    
    # nz =0
    # nt =n-1
    # for i in range(0,n,1):
    #     if arr[i] == 0:
    #         arr[nz],arr[i] = arr[i],arr[nz]
    #         nz = nz + 1
    #         i = i + 1
    #     elif arr[i] == 1:
    #         i = i + 1
    #         nz = i
    #     elif arr[i]==2 and arr[nt]==0:
    #         arr[nt],arr[i] = arr[i],arr[nt]
    #         nt = nt - 1
    #         i = i + 1
    #     elif arr[i]==2 and arr[nt]==1:
    #         arr[nt],arr[i] = arr[i],arr[nt]
    #         nt = nt - 1

            

            
            
   
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()

    sort012(arr, n)
    printList(arr, n)
    
    t -= 1