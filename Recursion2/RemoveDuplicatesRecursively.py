# Given a string S, remove consecutive duplicates from it recursively.
# Input Format :
# String S
# Output Format :
# Output string
# Constraints :
# 1 <= |S| <= 10^3
# where |S| represents the length of string
# Sample Input 1 :
# aabccba
# Sample Output 1 :
# abcba
# Sample Input 2 :
# xxxyyyzwwzzz
# Sample Output 2 :
# xyzwz

# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    n = len(string)
    if n==0 or n==1:
        return string
    smalloutput = removeConsecutiveDuplicates(string[1:])
    if string[0] == smalloutput[0]:
        return smalloutput
    else:
        return string[0] + smalloutput
    
    
    
    
# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
