# Given a string (let's say of length n), return all the subsequences of the given string.
# Subsequences contain all the strings of length varying from 0 to n. But the order of characters should remain the same as in the input string.
# Note: The order of subsequences are not important.
# Sample Input:
# abc
# Sample Output:
# "" (the double quotes just signifies an empty string, don't worry about the quotes)
# c 
# b 
# bc 
# a 
# ac 
# ab 
# abc 



def subsequences(str):
    arr = []
    if str == "":
        arr.append("")
        return arr
    
    arr = subsequences(str[1:])
    for i in range(len(arr)):
        arr.append(str[0]+arr[i])
        
    return arr

    
string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)
