# You have been given a random integer array/list(ARR) and a number X. Find and return the triplet(s) in the array/list which sum to X.
# Note :
# Given array/list can contain duplicate elements.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First line of each test case or query contains an integer 'N' representing the size of the first array/list.

# Second line contains 'N' single space separated integers representing the elements in the array/list.

# Third line contains an integer 'X'.
# Output format :
# For each test case, print the total number of triplets present in the array/list.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^3
# 0 <= X <= 10^9

# Time Limit: 1 sec
# Sample Input 1:
# 1
# 7
# 1 2 3 4 5 6 7 
# 12
# Sample Output 1:
# 5
# Sample Input 2:
# 2
# 7
# 1 2 3 4 5 6 7 
# 19
# 9
# 2 -5 8 -6 0 5 10 11 -3
# 10
# Sample Output 2:
# 0
# 5


#  Explanation for Input 2:
# Since there doesn't exist any triplet with sum equal to 19 for the first query, we print 0.

# For the second query, we have 5 triplets in total that sum up to 10. They are, (2, 8, 0), (2, 11, -3), (-5, 5, 10), (8, 5, -3) and (-6, 5, 11)

from sys import stdin
# merging two sorted arrays
def merge(arr,arr1,arr2):
    i,j,k = 0,0,0
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    while(i<len(arr1)):
        arr[k] = arr1[i]
        i += 1
        k += 1
    while(j<len(arr2)):
        arr[k] = arr2[j]
        j += 1
        k += 1
            
# merge_sort algorithm    
def merge_sort(arr):
    n = len(arr)
    if n==1 or n==0:
        return
    mid = n//2
    arr1,arr2 = [],[]
    arr1 = arr[0:mid]
    arr2 = arr[mid:]
    merge_sort(arr1)
    merge_sort(arr2)
    merge(arr,arr1,arr2)
        

        
def tripletSum(arr, n, num) :
    merge_sort(arr)
    count = 0
    for i in range(0,n,1):
        x = num-arr[i]
        k=i+1
        j=n-1
        while k<j:
            if arr[k] + arr[j] >x:
                j = j-1
            elif arr[k] + arr[j] <x:
                k = k + 1
            else:
                if arr[k] == arr[j]:
                    temp = j-k+1
                    count = count + ((temp)*(temp-1))//2
                    k=k+temp
                    j=j-temp
                elif (arr[k] == arr[k+1]) or (arr[j] == arr[j-1]):
                    tk = 1
                    while arr[k] == arr[k+tk]:
                        tk += 1
                    tj = 1
                    while arr[j] == arr[j-tj]:
                        tj += 1
                    count = count + tk*tj
                    k=k+tk
                    j=j-tj
                else:
                    k=k+1
                    j=j-1
                    count = count + 1
    return count    
    
    



#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(tripletSum(arr, n, num))

    t -= 1