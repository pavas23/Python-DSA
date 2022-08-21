# Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:
# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'
# If all the rules are followed by the given string, return true otherwise return false.
# Input format :
# String S
# Output format :
# 'true' or 'false'
# Constraints :
# 1 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# abb
# Sample Output 1 :
# true
# Sample Input 2 :
# abababa
# Sample Output 2 :
# false
# Explanation for Sample Input 2
# In the above example, a is not followed by either "a" or "bb", instead it's followed by # "b" which results in false to be returned.
## Read input as specified in the question.
## Print output as specified in the question.
def AB(s):
   if len(s)==0:
       return True
   if len(s)==1 and s=='a':
       return True
   if s[0]=='a':
        if s[1]=='a':
            return AB(s[1:])
        if s[1]=='b'  and s[2]=='b':
            return AB(s[3:])
        if s[1:]=='':
            return True
        else:
            return False   
s=input()
if AB(s):
    print('true')
else:
    print('false')
    
    
    
    
