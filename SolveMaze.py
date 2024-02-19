# solve maze using DFS
def solve_maze(maze):
    start_position = (0, 0)
    end_position = (len(maze) - 1, len(maze[0]) - 1)
    

    path=find_path(maze, start_position, end_position)
    if path:
        for t in path:
            row,col=t[0],t[1]
            maze[row][col]  =  "◍"
        return True
    return False        
              