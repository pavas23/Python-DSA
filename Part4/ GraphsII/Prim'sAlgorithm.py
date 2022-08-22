# Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
# Find and print the Minimum Spanning Tree (MST) using Prim's algorithm.
# For printing MST follow the steps -
# 1. In one line, print an edge which is part of MST in the format - 
# v1 v2 w
# where, v1 and v2 are the vertices of the edge which is included in MST and whose weight is w. And v1  <= v2 i.e. print the smaller vertex first while printing an edge.
# 2. Print V-1 edges in above format in different lines.
# Note : Order of different edges doesn't matter.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)
# Output Format :
# Print the MST, as described in the task.
# Constraints :
# 2 <= V, E <= 10^5
# 1 <= Wi <= 10^5
# Time Limit: 1 sec
# Sample Input 1 :
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8
# Sample Output 1 :
# 0 1 3
# 1 2 1
# 0 3 5

import sys

class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix =[[0 for i in range(self.nVertices)] for j in range(self.nVertices)]
        
    def addEdge(self,v1,v2,wt):
        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt
        return
    
    
    def __getMinVertex(self,visited,weight):
        minVertex = -1
        for i in range(self.nVertices):
            if(visited[i] is False and (minVertex== -1 or weight[i]<weight[minVertex])):
                minVertex = i
        return minVertex
        
    def prim(self):
        visited = [False for i in range(self.nVertices)]
        parent = [-1 for i in range(self.nVertices)]
        weight = [sys.maxsize for i in range(self.nVertices)]
        weight[0] = 0
        for i in range(self.nVertices-1):
            minVertex = self.__getMinVertex(visited,weight)
            visited[minVertex] = True
            for j in range(self.nVertices):
                if(self.adjMatrix[minVertex][j] > 0 and visited[j] is False):
                    if(weight[j] > self.adjMatrix[minVertex][j]):
                        weight[j] = self.adjMatrix[minVertex][j]
                        parent[j] = minVertex
        
        for i in range(1,self.nVertices):
            parentIndex = parent[i]
            wt = weight[i]
            if(i<parentIndex):
                print(str(i) + " " + str(parentIndex) + " " + str(wt))
            else:
                print(str(parentIndex) + " " + str(i) + " " + str(wt))
        
        return
    
  
v,e = [int(i) for i in input().split(" ")]
g = Graph(v)
for i in range(e):
    li = [int(j) for j in input().split(" ")]
    g.addEdge(li[0],li[1],li[2])
    
g.prim()