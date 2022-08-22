# Given a string, find and return all the possible permutations of the input string.
# Note : The order of permutations are not important.
# Sample Input :
# abc
# Sample Output :
# abc
# acb
# bac
# bca
# cab
# cba



def permutations(str):
    n = len(str)
    if n == 1:
        output = ""
        output += str[0]
        return output
    
    output = []
    arr = permutations(str[1:])
    for word in arr:
        output.append(str[0]+word)
        output.append(word+str[0])
        for i in range(len(word)):
            if i< len(word)-1:
                new_word = word[0:i+1] + str[0] + word[i+1:]
                output.append(new_word)

    return output
                
            
string = input()
ans = permutations(string)
for s in ans:
    print(s)



