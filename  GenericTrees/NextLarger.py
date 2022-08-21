# Given a generic tree and an integer n. Find and return the node with next larger element in the tree i.e. find a node with value just greater than n.
# Note: Return NULL if no node is present with the value greater than n.
# Input format :
# The first line of input contains data of the nodes of the tree in level order form. The order is: data for root node, number of children to root node, data of each of child nodes and so on and so forth for each node. The data of the nodes of the tree is separated by space.  
# The following line contains an integer, that denotes the value of n.
# Output format :
# The first and only line of output contains data of the node, whose data is just greater than n.
# Constraints:
# Time Limit: 1 sec
# Sample Input 1 :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# 18
# Sample Output 1 :
# 20
# Sample Input 2 :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# 21
# Sample Output 2:
# 30

from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def nextLargest(root, n):
    if root == None:
        return None
    arr = []
    if root.data > n:
        arr.append(root)
        
    for child in root.children:
        arr.append(nextLargest(child,n))
    
    if len(arr) != 0:
        min_node = arr[0]
    if len(arr) == 0:
        min_node = None
    
    for i in range(1,len(arr),1):
        if min_node != None:
            if min_node.data > arr[i].data:
                min_node = arr[i]
            
    return min_node

        
    
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
arr = list(int(x) for x in stdin.readline().strip().split())
n = int(input())
tree = createLevelWiseTree(arr)
if nextLargest(tree, n):
    print(nextLargest(tree, n).data)