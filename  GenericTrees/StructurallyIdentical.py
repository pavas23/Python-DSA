# Given two generic trees, return true if they are structurally identical. Otherwise return false.
# Structural Identical
# If the two given trees are made of nodes with the same values and the nodes are arranged in the same way, then the trees are called identical.  
# Input format :
# The first line of input contains data of the nodes of the first tree in level order form. The order is: data for root node, number of children to root node, data of each of child nodes and so on and so forth for each node. The data of the nodes of the tree is separated by space.  
# The following line of input contains data of the nodes of the second tree in level order form. The order is: data for root node, number of children to root node, data of each of child nodes and so on and so forth for each node. The data of the nodes of the tree is separated by space.
# Output format :
# The first and only line of output contains true, if the given trees are structurally identical and false, otherwise.
# Constraints:
# Time Limit: 1 sec
# Sample Input 1 :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# 10 3 20 30 40 2 40 50 0 0 0 0
# Sample Output 1 :
# true
# Sample Input 2 :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# 10 3 2 30 40 2 40 50 0 0 0 0
# Sample Output 2:
# false

from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        
def storingTree(root):
    arr = []
    if root == None:
        return arr
    arr.append(root.data)
    for child in root.children:
        arr.append(child.data)
    for child in root.children:
        storingTree(child)
    return arr


def isIdentical(root1,root2):
    if root1.data != root2.data:
        return False
    flag = 0
    arr1 = storingTree(root1)
    arr2 = storingTree(root2)
    n1 = len(arr1)
    n2 = len(arr2)
    if n1 != n2:
        return False
    else:
        for i in range(n1):
            if arr1[i] != arr2[i]:
                flag = 1
                break
    if flag == 1:
        return False
    return True
                

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr1 = list(int(x) for x in stdin.readline().strip().split())
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in stdin.readline().strip().split())
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')