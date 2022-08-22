# Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), find and print the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.
# Find the path using DFS and print the first path that you encountered.
# Note:
# 1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
# 2. E is the number of edges present in graph G.
# 3. Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
# 4. Save the input graph in Adjacency Matrix.
# Input Format :
# The first line of input contains two integers, that denote the value of V and E.
# Each of the following E lines contains two integers, that denote that there exists an edge between vertex 'a' and 'b'.
# The following line contain two integers, that denote the value of v1 and v2.
# Output Format :
# Print the path from v1 to v2 in reverse order.
# Constraints :
# 2 <= V <= 1000
# 1 <= E <= (V * (V - 1)) / 2
# 0 <= a <= V - 1
# 0 <= b <= V - 1
# 0 <= v1 <= 2^31 - 1
# 0 <= v2 <= 2^31 - 1
# Time Limit: 1 second
# Sample Input 1 :
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# 1 3
# Sample Output 1 :
# 3 0 1
# Sample Input 2 :
# 6 3
# 5 3
# 0 1
# 3 4
# 0 3
# Sample Output 2 :

#Write your code here
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 8)
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(self.nVertices)] for j in range(self.nVertices)]
        
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        return
    
    
    
    def __getPathHelper(self,v1,v2,visited,output):
        visited[v1] = True
        # if v1 == v2:
        #     visited[v2] == True
        #     output.append(v2)
        #     return output
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i] == 1 and visited[i] == False:
                visited[i] = True
                if i == v2:
                    output.append(v2)
                    output.append(v1)
                    return output
                else:
                    output = self.__getPathHelper(i,v2,visited,output)
                    if output != None:
                        output.append(v1)
                        return output       
        return None
                        
                   
    def getPath(self,v1,v2):
        visited = [False for i in range(self.nVertices)]
        output = []
        return self.__getPathHelper(v1,v2,visited,output)
        

    
    
v,e = [int(i) for i in input().split(" ")]
g = Graph(v)
if e != 0:
    for i in range(e):
        v1,v2 = [int(i) for i in input().split(" ")]
        g.addEdge(v1,v2)
    v1,v2 = [int(j) for j in input().split(" ")]
    ans = g.getPath(v1,v2)
    if ans == None:
        print()   
    else:  
        for i in ans:
            print(i,end=" ")
else:
    print()
    