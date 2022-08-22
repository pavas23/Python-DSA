# Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
# Find and print the shortest distance from the source vertex (i.e. Vertex 0) to all other vertices (including source vertex also) using Dijkstra's Algorithm.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)
# Output Format :
# For each vertex, print its vertex number and its distance from source, in a separate line. The vertex number and its distance needs to be separated by a single space.
# Note : Order of vertices in output doesn't matter.
# Constraints :
# 2 <= V, E <= 10^5
# Time Limit: 1 sec
# Sample Input 1 :
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8
# Sample Output 1 :
# 0 0
# 1 3
# 2 4
# 3 5

import sys
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(self.nVertices)] for j in range(self.nVertices)]
        
    def addEdge(self,v1,v2,dist):
        self.adjMatrix[v1][v2] = dist
        self.adjMatrix[v2][v1] = dist
        return
    
    def __getminVertex(self,visited,distance):
        minVertex = -1
        for i in range(self.nVertices):
            if(visited[i] is False and (minVertex == -1 or distance[i]<distance[minVertex])):
                minVertex = i
        return minVertex
        
        
        
    def dijkstra(self):
        visited = [False for i in range(self.nVertices)]
        distance = [sys.maxsize for i in range(self.nVertices)]
        distance[0] = 0
        for i in range(self.nVertices-1):
            minVertex = self.__getminVertex(visited,distance)
            visited[minVertex] = True
            for j in range(self.nVertices):
                if(self.adjMatrix[minVertex][j] >0 and visited[j] is False):
                    if(distance[j] > self.adjMatrix[minVertex][j]+distance[minVertex]):
                        distance[j] = self.adjMatrix[minVertex][j] + distance[minVertex]
        
        for i in range(self.nVertices):
            v  = i
            dis = distance[i]
            print(str(v) + " " + str(dis))
        return
                            
v,e = [int(i) for i in input().split()]
g = Graph(v)
for i in range(e):
    li1 = [int(j) for j in input().split(" ")]
    g.addEdge(li1[0],li1[1],li1[2])
    
g.dijkstra()
    