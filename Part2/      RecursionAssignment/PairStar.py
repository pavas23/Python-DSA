# Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
# Input format :
# String S
# Output format :
# Modified string
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# hello
# Sample Output 1:
# hel*lo
# Sample Input 2 :
# aaaa
# Sample Output 2 :
# a*a*a*a

## Read input as specified in the question.
## Print output as specified in the question.
def pair_star(s):
    n = len(s)
    if n==0 or n==1:
        return s
    s1 = s[1:]
    smalloutput = pair_star(s1)
    if s[0] == s1[0]:
        return s[0]+ "*" + smalloutput
    else:
        return s[0] + smalloutput
    

s = input()
print(pair_star(s))


