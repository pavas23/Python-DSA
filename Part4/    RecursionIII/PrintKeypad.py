# Given an integer n, using phone keypad find out and print all the possible strings that can be made using digits of input n.
# Note : The order of strings are not important. Just print different strings in new lines.
# Input Format :
# Integer n
# Output Format :
# All possible strings in different lines
# Constraints :
# 1 <= n <= 10^6
# Sample Input:
# 23
# Sample Output:
# ad
# ae
# af
# bd
# be
# bf
# cd
# ce
# cf


def printKeypad(n,curr_out,char_arr):
    
#     if n == n%10:
#         for i in range(len(char_arr[n-2])):
#             print(char_arr[n-2][i])
#         return
    
    if n == 0:
        print(curr_out)
        return
    
    n1 = n
    y = 0
    if n1 <10:
        first_digit = n1
    else:
        while(n1>10):
            y += 1
            n1 = int(n1/10)
            first_digit = n1
    
    n = n - (first_digit*(10**y))
    
    for i in range(len(char_arr[first_digit-2])):
        printKeypad(n,curr_out+char_arr[first_digit-2][i],char_arr)
        
    

n = int(input())
char_arr = [["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
printKeypad(n,"",char_arr)
