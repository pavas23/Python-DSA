
def printPathHelper(x,y,maze,n,solution):
    if x==n-1 and y == n-1:
        solution[x][y] = 1
        print(solution)
        return
    
    if x<0 or y<0 or x>=n or y>=n or maze[x][y] == 0 or solution[x][y] == 1:
        return
    
    solution[x][y] = 1
    printPathHelper(x+1,y,maze,n,solution)
    printPathHelper(x,y+1,maze,n,solution)
    printPathHelper(x-1,y,maze,n,solution)
    printPathHelper(x,y-1,maze,n,solution)
    solution[x][y] = 0
    return

def printPath(maze):
    n = len(maze)
    solution = [[0 for i in range(n)] for j in range(n)]
    printPathHelper(0,0,maze,n,solution)


n = int(input())
maze = []
for i in range(0,n,1):
    row = [int(i) for i in input().split()]
    maze.append(row)

printPath(maze)


    