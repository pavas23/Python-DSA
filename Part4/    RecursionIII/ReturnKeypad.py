# Given an integer n, using phone keypad find out and return all the possible strings that can be made using digits of input n.
# Note : The order of strings are not important.
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


def keypad(n,char_arr):
    
    if int(n/10) == 0:
        arr = []
        for i in range(len(char_arr[n-2])):
            arr.append(char_arr[n-2][i])
        return arr
    
    last_digit = n%10
    new_num = int(n/10)
    
    small_output = keypad(new_num,char_arr)
    output = []
    for i in range(len(small_output)):
        for j in range(len(char_arr[last_digit-2])):
            output.append(small_output[i]+char_arr[last_digit-2][j])
    
    return output
            
    
    


n = int(input())

char_arr = [["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]

ans = keypad(n,char_arr)
for s in ans:
    print(s)
    
    