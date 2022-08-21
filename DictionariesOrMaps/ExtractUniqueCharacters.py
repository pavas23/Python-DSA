# Given a string S, you need to remove all the duplicates. That means, the output string should contain each character only once. The respective order of characters should remain same, as in the input string.
# Input format:
# The first and only line of input contains a string, that denotes the value of S.
# Output format :
# The first and only line of output contains the updated string, as described in the task.
# Constraints :
# 0 <= Length of S <= 10^8
# Time Limit: 1 sec
# Sample Input 1 :
# ababacd
# Sample Output 1 :
# abcd
# Sample Input 2 :
# abcde
# Sample Output 2 :
# abcde

def uniqueChar(s):
    new = ''
    for i in s:
        if i not in new:
            new+=i
    return new  



# Main 
s=input() 
print(uniqueChar(s))