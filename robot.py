'''
@date - Dec 2017.
@author: Diwas Poudel
'''

from copy import copy
def robot(grid):
    rows = len(grid)
    cols = len(grid[0])
    path = []
    cost = []
    
    #Insert zeros in the array
    for i in range(0,rows):
        path.insert(0, [])
        cost.insert(0, [])
    
    #Create array of path and cost empty
    for i in range(0,rows):
        for j in range(0,cols):
            path[i].append([])
            cost[i].append([0]) 
    
    #Go through rows and column, collect coins, add paths
    for i in range(rows-1,-1,-1):
        for j in range(cols-1,-1,-1):
            m, n, o = 0, 0, 0
            
            if i+1 < rows:
                n = cost[i+1][j] + grid[i][j]
            if j+1 < cols:
                m = cost[i][j+1] + grid[i][j]
                
            o = grid[i][j]
            cost[i][j] = max(m,n,o)
            
            if j+1 < cols and m == max(m,n):
                path[i][j] = copy(path[i][j+1])
                path[i][j].insert(0, "Right")
                
            elif i + 1 < rows and n == max(m,n):
                path[i][j] = copy(path[i+1][j])
                path[i][j].insert(0, "Down")
                
    return cost[0][0], path[0][0]

#Grid with coins
grid = [[0,0,0,1,0,0], [0,1,0,0,2,0], [0,0,0,1,0,0], [0,0,0,1,0,1], [0,0,2,0,0,1], [3,0,0,1,0,0]]
print("The max values of coins is: " + str(robot(grid)[0]))
print("The path is: " + str(robot(grid)[1]))


