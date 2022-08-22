# Sort an array A using Quick Sort.
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
# 1 5 2 7 3
# Sample Output 2 :
# 1 2 3 5 7 

def partition(arr,si,ei):
    pivot = arr[si]
    count = 0
    for i in range(si,ei+1,1):
        if arr[i] < pivot:
            count += 1
    arr[si],arr[si+count] = arr[si+count],arr[si]
    pivot_index = si+count
    pivot = arr[si+count]
    i,j = si,ei
    while(i<j):
        if arr[i] < pivot:
            i += 1
        elif arr[j] >= pivot:
            j -= 1
        else:
            arr[i],arr[j] = arr[j],arr[i]
    
    return pivot_index        
    

def quickSort(arr,si,ei):
    if si>=ei:
        return 
    pivot_index = partition(arr,si,ei)
    quickSort(arr,si,pivot_index-1)
    quickSort(arr,pivot_index+1,ei)
    

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)
