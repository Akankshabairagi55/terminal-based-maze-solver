import random
def generate_maze(n):
    maze = [['▓' if random.random() < 0.25 else '◌' for _ in range(n)] for _ in range(n)]
    maze[0][0] = "S"
    maze[n-1][n-1] = "E"
    return maze