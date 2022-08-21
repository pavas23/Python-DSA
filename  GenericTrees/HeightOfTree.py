# Given a generic tree, find and return the height of given tree.
# Input Format:
# The first line of input contains data of the nodes of the tree in level order form. The order is: data for root node, number of children to root node, data of each of child nodes and so on and so forth for each node. The data of the nodes of the tree is separated by space.  
# Output Format :
# The first and only line of output prints the height of the given generic tree.
# Constraints:
# Time Limit: 1 sec
# Sample Input 1:
# 10 3 20 30 40 2 40 50 0 0 0 0 
# Sample Output 1:
# 3

from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)



def heightOfTree(root):
    if root == None:
        return 0
    height_arr = []
    height_arr.append(1)
    flag = 0
    for child in root.children:
        flag = 1
        height_arr.append(heightOfTree(child))
    if flag == 1:
        return max(height_arr) + 1
    else:
        return max(height_arr)

    
    
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
arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
root = createLevelWiseTree(arr)
print(heightOfTree(root))
