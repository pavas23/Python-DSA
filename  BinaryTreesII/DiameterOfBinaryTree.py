# For a given Binary of type integer, find and return the ‘Diameter’.
# Diameter of a Tree
# The diameter of a tree can be defined as the maximum distance between two leaf nodes.
# Here, the distance is measured in terms of the total number of nodes present along the path of the two leaf nodes, including both the leaves.
# Example:
# alt txt

# The maximum distance can be seen between the leaf nodes 8 and 9. 
# The distance is 9 as there are a total of nine nodes along the longest path from 8 to 9(inclusive of both). Hence the diameter according to the definition will be 9.
# Input Format:
# The first and the only line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.
# Output Format:
# The only line of output prints an integer, representing the diameter of the tree.
# Note:
# You are not required to print anything explicitly. It has already been taken care of.
# Constraints:
# 1 <= N <= 10^5
# Where N is the total number of nodes in the binary tree.

# Time Limit: 1 sec
# Sample Input 1:
# 2 4 5 6 -1 -1 7 20 30 80 90 -1 -1 8 -1 -1 9 -1 -1 -1 -1 -1 -1 
# Sample Output 1:
# 9
# Sample Input 2:
# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# Sample Output 2:
# 5

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




def diameterOfBinaryTree(root) :
    if root == None:
        return 0,0
    if root.left == None and root.right ==None:
        return 1,0
    lh,ld = diameterOfBinaryTree(root.left)
    rh,rd = diameterOfBinaryTree(root.right)
    return max(lh,rh)+1,max(lh+rh,ld,rd)+1
    


