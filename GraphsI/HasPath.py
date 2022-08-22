# Given an undirected graph G(V, E) and two vertices v1 and v2 (as integers), check if there exists any path between them or not. Print true if the path exists and false otherwise.
# Note:
# 1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
# 2. E is the number of edges present in graph G.
# Input Format :
# The first line of input contains two integers, that denote the value of V and E.
# Each of the following E lines contains two integers, that denote that there exists an edge between vertex 'a' and 'b'.
# The following line contain two integers, that denote the value of v1 and v2.
# Output Format :
# The first and only line of output contains true, if there is a path between v1 and v2 and false otherwise.
# Constraints :
# 0 <= V <= 1000
# 0 <= E <= 1000
# 0 <= a <= V - 1
# 0 <= b <= V - 1
# 0 <= v1 <= V - 1
# 0 <= v2 <= V - 1
# Time Limit: 1 second
# Sample Input 1 :
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# 1 3
# Sample Output 1 :
# true
# Sample Input 2 :
# 6 3
# 5 3
# 0 1
# 3 4
# 0 3
# Sample Output 2 :
# false

class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(self.nVertices)] for j in range(self.nVertices)]
        
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        return
    
    def hasPath(self,v1,v2):
        visited = [False for i in range(self.nVertices)]
        return self.__hasPathHelper(v1,v2,visited)
    
    def __hasPathHelper(self,v1,v2,visited):
        visited[v1] = True
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i] == 1 and visited[i] is False:
                if i == v2:
                    return True
                
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i] == 1 and visited[i] is False:
                if self.__hasPathHelper(i,v2,visited):
                    return True
        
        return False
        
            
        
li = [int(i) for i in input().split(" ")]
v = li[0]
e = li[1]
g = Graph(v)
for j in range(e):
    li1 = [int(i) for i in input().split(" ")]
    v1 = li1[0]
    v2 = li1[1]
    g.addEdge(v1,v2)

li2 = [int(i) for i in input().split(" ")]
v1,v2 = li2[0],li2[1]
if g.hasPath(v1,v2):
    print("true")
else:
    print("false")
    