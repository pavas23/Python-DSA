# Check whether a given String S is a palindrome using recursion. Return true or false.
# Input Format :
# String S
# Output Format :
# 'true' or 'false'
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# racecar
# Sample Output 1:
# true
# Sample Input 2 :
# ninja
# Sample Output 2:
# false

## Read input as specified in the question.
## Print output as specified in the question.
def check_palindrome(s):
    n = len(s)
    if n==0 or n==1:
        return s
    smalloutput = check_palindrome(s[1:])
    str1 =""
    str1 = smalloutput + s[0]
    return str1
    

s = input()
str2 = check_palindrome(s)
if str2 == s:
    print("true")
else:
    print("false")
