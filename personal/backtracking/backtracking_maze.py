def findAllPaths(maze,r,c,result):
    if r==len(maze)-1 and c == len(maze)-1:
        print(result)
        return
    
    if not maze[r][c]:
        return
    
    #Changing state that visited
    maze[r][c]=False
    #Can go D,U,R,L with edge conditions, but we need to modify the maze
    if r<len(maze)-1:        
        findAllPaths(maze,r=r+1,c=c+0,result= result+'D')
    if c<len(maze)-1:
        findAllPaths(maze,r,c=c+1,result= result+'R')
    if r>0:
        maze[r][c]=False
        findAllPaths(maze,r=r-1,c=c+0,result= result+'U')
    if c>0:
        maze[r][c]=False
        findAllPaths(maze,r=r,c=-1,result=result+'L')
    
    #Reverting the change before exiting
    maze[r][c]=True
    
maze = [[True,True,True],
        [True,True,True],
        [True,True,True]]
findAllPaths(maze,r=0,c=0,result='')