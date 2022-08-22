# For a given expression in the form of a string, find the minimum number of brackets that can be reversed in order to make the expression balanced. The expression will only contain curly brackets.
# If the expression can't be balanced, return -1.
# Example:
# Expression: {{{{
# If we reverse the second and the fourth opening brackets, the whole expression will get balanced. Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.

# Expression: {{{
# In this example, even if we reverse the last opening bracket, we would be left with the first opening bracket and hence will not be able to make the expression balanced and the output will be -1.
# Input Format :
# The first and the only line of input contains a string expression, without any spaces in between.
# Output Format :
# The only line of output will print the number of reversals required to balance the whole expression. Prints -1, otherwise.
# Note:
# You don't have to print anything. It has already been taken care of.
# Constraints:
# 0 <= N <= 10^6
# Where N is the length of the expression.

# Time Limit: 1sec
# Sample Input 1:
# {{{
# Sample Output 1:
# -1
# Sample Input 2:
# {{{{}}
# Sample Output 2:
# 1


from sys import stdin

def countBracketReversals(inputString) :
    # s = inputString
    # n = len(s)
    # count,count1 = 0,0
    # for i in range(0,n,1):
    #     if s[i] == "{":
    #         count += 1
    #     elif s[i] == "}":
    #         count1 += 1
    # if count == 0:
    #     if count1 %2 == 0:
    #         return count1//2
    # if count1 == 0:
    #     if count%2 ==0:
    #         return count//2
    # if (count+count1)%2 == 0:
    #     return count + 1
    # else:
    #     return -1
    stack=[]
    count=0
    for ele in inputString:
        if ele=='}':
            if len(stack)>0:
                x=stack.pop()
                if x=='{':
                    pass
                else:
                    stack.append(x)
                    stack.append(ele)
            else:
                stack.append(ele)
        else:
            stack.append(ele)
    for i in range(len(stack)):
        if stack[i]=="}":
            count+=1
    if count>0:
        if count%2==0:
            if (len(stack)-count)%2==0:
                return len(stack)//2
            else:
                return -1
        else:
            eve=count//2
            clo=(len(stack)-count)//2
            return eve+clo+2
    if len(stack)%2==0:
        return len(stack)//2
    else:
        return -1

#main
print(countBracketReversals(stdin.readline().strip()))