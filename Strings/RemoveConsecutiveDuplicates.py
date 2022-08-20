# For a given string(str), remove all the consecutive duplicate characters.
# Example:
# Input String: "aaaa"
# Expected Output: "a"

# Input String: "aabbbcc"
# Expected Output: "abc"
#  Input Format:
# The first and only line of input contains a string without any leading and trailing spaces. All the characters in the string would be in lower case.
# Output Format:
# The only line of output prints the updated string.
# Note:
# You are not required to print anything. It has already been taken care of.
# Constraints:
# 0 <= N <= 10^6
# Where N is the length of the input string.

# Time Limit: 1 second
# Sample Input 1:
# aabccbaa
# Sample Output 1:
# abcba
# Sample Input 2:
# xxyyzxx
# Sample Output 2:
# xyzx


from sys import stdin

# def removeConsecutiveDuplicates(string):
#     n = len(string)
#     i = 0
#     str1 = []
#     j = 0
#     if n<=1:
#         str1 = string
#     else:
#         for j in range(0,n-1,1):
#             if string[i] != string[i+1]:
#                 str1[j] = string[i]
#                 j += 1
#             else:
#                 while(string[i]==string[i+1]):
#                     str1[j] = string[i] 
#                     i = i + 1
#                     j = j + 1
#     return str1        
# # 
from sys import stdin

def removeConsecutiveDuplicates(string) :
    n = len(string)
    if n ==0:
        return string
    answer = ""
    startindex = 0
    while(startindex<n):
        unique_char = string[startindex]
        nextuniquecharindex = startindex + 1
        
        while((nextuniquecharindex<n) and (string[nextuniquecharindex]==unique_char)):
            nextuniquecharindex += 1
        answer +=  unique_char
        startindex = nextuniquecharindex
    return answer    
    
    #ind_arr=[-2]*123
    #new_str=""
    #for i in range (len(string)):
    #    ele=string[i]
    #    if(ind_arr[ord(ele)]<i-1):
    #        new_str=new_str+ele
    #    ind_arr[ord(ele)]=i
    #return new_str
	
   
#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)