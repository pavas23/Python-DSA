# Given a string, find and print all the possible permutations of the input string.
# Note : The order of permutations are not important. Just print them in different lines.
# Sample Input :
# abc
# Sample Output :
# abc
# acb
# bac
# bca
# cab
# cba

import sys
sys.setrecursionlimit(10**6)

        
def printPermutations(str,output):
    if str == "":
        print(output)
        return
    
    for i in range(len(str)):
        question_str = ""
        question_str = str[0:i] + str[i+1:]
        printPermutations(str[0:i] + str[i+1:],output+str[i])

    
string = input()
printPermutations(string,"")
