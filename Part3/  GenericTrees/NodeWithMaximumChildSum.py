# Given a generic tree, find and return the node for which sum of its data and data of all its child nodes is maximum. In the sum, data of the node and data of its immediate child nodes has to be taken.
# Input format :
# The first line of input contains data of the nodes of the tree in level order form. The order is: data for root node, number of children to root node, data of each of child nodes and so on and so forth for each node. The data of the nodes of the tree is separated by space. 
# Output format :
# The first and only line of output contains the data of the node with maximum sum, as described in the task.
# Constraints:
# Time Limit: 1 sec
# Sample Input 1 :
# 5 3 1 2 3 1 15 2 4 5 1 6 0 0 0 0
# Sample Output 1 :
# 1

from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def sum(self):
        ans = self.data
        for child in self.children:
            ans += child.data
        return ans

def maxSumNode(root):
    if root == None:
        return None
    li_node = []
    li_sum = []
    sum1 = root.data
    for child in root.children:
        a,b = maxSumNode(child)
        li_node.append(a)
        li_sum.append(b)
        sum1 += child.data
    max_node = root
    max_value = sum1
    for j in range(len(li_sum)):
        if sum1 < li_sum[j]:
            max_value = li_sum[j]
            max_node =  li_node[j]
    return max_node,max_value

        
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
tree = createLevelWiseTree(arr)
node , data = maxSumNode(tree)
print(node.data)
