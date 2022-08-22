# You are given a Binary Tree of type integer, a target node, and an integer value K.
# Print the data of all nodes that have a distance K from the target node. The order in which they would be printed will not matter.
# Example:
# For a given input tree(refer to the image below):
# 1. Target Node: 5
# 2. K = 2
# alt txt

# Starting from the target node 5, the nodes at distance K are 7 4 and 1.
# Input Format:
# The first line of input will contain the node data, all separated by a single space. Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.

# The second line of input contains two integers separated by a single space, representing the value of the target node and K, respectively.
# Output Format:
# All the node data at distance K from the target node will be printed on a new line.

# The order in which the data is printed doesn't matter.
# Constraints:
# 1 <= N <= 10^5
# Where N is the total number of nodes in the binary tree.

# Time Limit: 1 sec
# Sample Input 1:
# 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# 3 1
# Sample Output 1:
# 9
# 6
# Sample Input 2:
# 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1
# 3 3
# Sample Output 2:
# 4
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
        
def printkDistanceNodeDown(root, k):
    if root is None or k< 0 :
        return
     
    if k == 0 :
        print(root.data)
        return
     
    printkDistanceNodeDown(root.left, k-1)
    printkDistanceNodeDown(root.right, k-1)


def nodesAtDistanceK(root, target, k) :
     
    # Base Case 1 : IF tree is empty return -1
    if root is None:
        return -1

    if root.data == target:
        printkDistanceNodeDown(root, k)
        return 0
     
    # Recur for left subtree
    dl = nodesAtDistanceK(root.left, target, k)
     
    # Check if target node was found in left subtree
    if dl != -1:
         
        # If root is at distance k from target, print root
        # Note: dl is distance of root's left child
        # from target
        if dl +1 == k :
            print(root.data)
     
        else:
            printkDistanceNodeDown(root.right, k-dl-2)

        return 1 + dl
 
    dr = nodesAtDistanceK(root.right, target, k)
    if dr != -1:
        if (dr+1 == k):
            print(root.data)
        else:
            printkDistanceNodeDown(root.left, k-dr-2)
        return 1 + dr
 
    # If target was neither present in left nor in right subtree
    return -1