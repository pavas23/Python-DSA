# Given k, find the geometric sum i.e.
# 1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
# using recursion.
# Input format :
# Integer k
# Output format :
# Geometric sum (upto 5 decimal places)
# Constraints :
# 0 <= k <= 1000
# Sample Input 1 :
# 3
# Sample Output 1 :
# 1.87500
# Sample Input 2 :
# 4
# Sample Output 2 :
# 1.93750
# Explanation for Sample Input 1:
# 1+ 1/(2^1) + 1/(2^2) + 1/(2^3) = 1.87500

## Read input as specified in the question.
## Print output as specified in the question
def sum_of_gp(k):
    if k==0:
        return 1
    smalloutput = sum_of_gp(k-1)
    x = 1/(2**k)+smalloutput
    return x

    
k = int(input())
a = sum_of_gp(k)
print(str.format('{0:.5f}', a))

