# You have been given two stacks that can store integers as the data. Out of the two given stacks, one is populated and the other one is empty. You are required to write a function that reverses the populated stack using the one which is empty.
# For Example:
# Alt txt

# Input Format :
# The first line of input contains an integer N, denoting the total number of elements in the stack.

# The second line of input contains N integers separated by a single space, representing the order in which the elements are pushed into the stack.
# Output Format:
# The only line of output prints the order in which the stack elements are popped, all of them separated by a single space. 
# Note:
# You are not required to print the expected output explicitly, it has already been taken care of. Just make the changes in the input stack itself.
# Constraints:
# 1 <= N <= 10^3
# -2^31 <= data <= 2^31 - 1

# Time Limit: 1sec 
# Sample Input 1:
# 6
# 1 2 3 4 5 10
# Note:
# Here, 10 is at the top of the stack.
# Sample Output 1:
# 1 2 3 4 5 10
# Note:
# Here, 1 is at the top of the stack.
# Sample Input 2:
# 5
# 2 8 15 1 10
# Sample Output 2:
# 2 8 15 1 10

from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def reverseStack(inputStack, extraStack) :
    extraStack = []
    n = len(inputStack)
    if n == 1 or n== 0:
        return 
    for i in range(n-1,0,-1):
        extraStack.append(inputStack[i])
        inputStack.pop()
    x = inputStack[0]
    inputStack.pop()
    for i in range(len(extraStack)-1,-1,-1):
        inputStack.append(extraStack[i])
        extraStack.pop()
    reverseStack(inputStack,extraStack)
    inputStack.append(x)
        
'''-------------- Utility Functions --------------'''

#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Taking input using fast I/o method
def takeInput() :
	size = int(stdin.readline().strip())
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, stdin.readline().strip().split(" ")))
	inputStack = values

	return inputStack


# Main
inputStack = takeInput()
emptyStack = []

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")