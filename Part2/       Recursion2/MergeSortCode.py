# Sort an array A using Merge Sort.
# Change in the input array itself. So no need to return or print anything.
# Input format :
# Line 1 : Integer n i.e. Array size
# Line 2 : Array elements (separated by space)
# Output format :
# Array elements in increasing order (separated by space)
# Constraints :
# 1 <= n <= 10^3
# Sample Input 1 :
# 6 
# 2 6 8 5 4 3
# Sample Output 1 :
# 2 3 4 5 6 8
# Sample Input 2 :
# 5
# 2 1 5 2 3
# Sample Output 2 :
# 1 2 2 3 5 

def mergeSort(arr):
    n = len(arr)
    if n==0 or n==1:
        return arr
    mid = (0+n-1)//2
    arr1 = arr[0:mid+1]
    arr2 = arr[mid+1:]
    mergeSort(arr1)
    mergeSort(arr2)
    i,j =0,0
    k = 0
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            k = k  + 1
            i += 1
        elif arr1[i] >= arr2[j]:
            arr[k] = arr2[j]
            k += 1
            j += 1
    while(i<len(arr1)):
        arr[k] = arr1[i]
        k += 1
        i += 1
    while(j<len(arr2)):
        arr[k] = arr2[j]
        k += 1
        j += 1
    
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)
