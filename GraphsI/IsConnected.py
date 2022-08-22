# Given an undirected graph G(V,E), check if the graph G is connected graph or not.
# Note:
# 1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
# 2. E is the number of edges present in graph G.
# Input Format :
# The first line of input contains two integers, that denote the value of V and E.
# Each of the following E lines contains two integers, that denote that there exists an edge between vertex a and b.
# Output Format :
# The first and only line of output contains "true" if the given graph is connected or "false", otherwise.
# Constraints :
# 0 <= V <= 1000
# 0 <= E <= (V * (V - 1)) / 2
# 0 <= a <= V - 1
# 0 <= b <= V - 1
# Time Limit: 1 second
# Sample Input 1:
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# Sample Output 1:
# true
# Sample Input 2:
# 4 3
# 0 1
# 1 3 
# 0 3
# Sample Output 2:
# false 
# Sample Output 2 Explanation
# The graph is not connected, even though vertices 0,1 and 3 are connected to each other but there isn’t any path from vertices 0,1,3 to vertex 2. 

# Write your code here
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 8)
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix =[[0 for i in range(self.nVertices)] for j in range(self.nVertices)]
    
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        return
    
    def __isConnectedHelper(self,sv,visited):
        visited[sv] = True
        for i in range(self.nVertices):
            if(self.adjMatrix[sv][i] == 1 and visited[i] == False):
                visited[i] = True
                self.__isConnectedHelper(i,visited)
        return
        
        
        
    def isConnected(self):
        visited = [False for i in range(self.nVertices)]
        sv = 0
        self.__isConnectedHelper(sv,visited)
        for i in range(self.nVertices):
            if(visited[i] == False):
                return False
        return True
    
v,e = [int(i) for i in input().split(" ")]
if v==0:
    print('true')
else:
    if(e<v-1):
        print('false')
    else:
        g = Graph(v)
        for i in range(e):
            v1,v2 = [int(i) for i in input().split(" ")]
            g.addEdge(v1,v2)
        ans = g.isConnected()
        if(ans == True):
            print('true')
        else:
            print('false')
        
        
        