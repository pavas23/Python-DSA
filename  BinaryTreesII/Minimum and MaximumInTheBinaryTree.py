# For a given a Binary Tree of type integer, find and return the minimum and the maximum data values.
# Return the output as an object of Pair class, which is already created.
# Note:
# All the node data will be unique and hence there will always exist a minimum and maximum node data.
# Input Format:
# The first and the only line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.
# Output Format:
# The only line of output prints two integers denoting the minimum and the maximum data values respectively. A single line will separate them both.
# Constraints:
# 2 <= N <= 10^5
# Where N is the total number of nodes in the binary tree.

# Time Limit: 1 sec
# Sample Input 1:
# 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
# Sample Output 1:
# 1 14
# Sample Input 2:
# 10 20 60 -1 -1 3 50 -1 -1 -1 -1 
# Sample Output 2:
# 3 60

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



#Representation of the Pair Class
class Pair :

    def __init__(self, minimum, maximum) :
        self.minimum = minimum
        self.maximum = maximum



def getMinAndMax(root) :
    if root == None:
        return None,None
    elif root.left == None and root.right == None:
        return root.data,root.data
    
    elif root.left == None and root.right != None:
        min,max = getMinAndMax(root.right)
        if max > root.data:
            newmax = max
        else:
            newmax = root.data
        if root.data < min:
            newmin = root.data
        else:
            newmin = min
        return newmin,newmax
    
    elif root.right == None and root.left != None:
        min,max = getMinAndMax(root.left)
        if max > root.data:
            newmax = max
        else:
            newmax = root.data
        if root.data < min:
            newmin = root.data
        else:
            newmin = min
        return newmin,newmax
    
        
    elif root.left != None and root.right != None:
        left_min, left_max = getMinAndMax(root.left)
        right_min,right_max = getMinAndMax(root.right)
        if left_min < right_min:
            min = left_min
        else:
            min = right_min
        if right_max > left_max:
            max = right_max
        else:
            max = left_max
        if max > root.data:
            newmax = max
        else:
            newmax = root.data
        if root.data < min:
            newmin = root.data
        else:
            newmin = min
        return newmin,newmax