# Given an array of length N, you need to find and print the sum of all elements of the array.
# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Output Format :
# Sum
# Constraints :
# 1 <= N <= 10^6
# Sample Input :
# 3
# 9 8 9
# Sample Output :
# 26

n = int(input())
a = input()
b = a.split()
li = []

for i in b:
    x = int(i)
    li.append(x)

sum = 0  

for j in li:
    sum = sum + j

print(sum)

    