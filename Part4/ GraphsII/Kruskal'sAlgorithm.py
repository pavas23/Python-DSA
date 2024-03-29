# Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
# Find and print the Minimum Spanning Tree (MST) using Kruskal's algorithm.
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
# Time Limit: 1 sec
# Sample Input 1 :
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8
# Sample Output 1 :
# 1 2 1
# 0 1 3
# 0 3 5


class Edge:
    def __init__(self,src,dest,wt):
        self.src = src
        self.dest = dest
        self.wt = wt



def getParent(v,parent_arr):
    if(v == parent_arr[v]):
        return v
    return getParent(parent_arr[v],parent_arr)
        
            
 
def Kruskal(edges,nVertices):
    i = 0
    count = 0
    output = []
    edges = sorted(edges,key = lambda edge:edge.wt)
    
    while count < nVertices-1:
        srcParent = getParent(edges[i].src,parent_arr)
        destParent = getParent(edges[i].dest,parent_arr)
        
        if srcParent != destParent:
            output.append(edges[i])
            parent_arr[srcParent] = destParent
            count += 1
        i += 1
    return output
    
    
edges = []

v,e = [int(i) for i in input().split(" ")]
parent_arr = [i for i in range(v)]
for i in range(e):
    li1 = [int(i) for i in input().split(" ")]