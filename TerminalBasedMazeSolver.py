# Import necessary modules
import random  # For generating random numbers
import os      # For system-related operations
os.system('color')  # Set color settings for Windows terminal
from termcolor import colored  # For adding color to text
from collections import deque   # For implementing the deque data structure

# Function to generate a maze
def generate_maze(n):
    # Generate a 2D list representing the maze
    maze = [['▓' if random.random() < 0.25 else '◌' for _ in range(n)] for _ in range(n)]
    # Mark the start and end points
    maze[0][0] = "S"
    maze[n-1][n-1] = "E"
    return maze

# Function to print the maze with special formatting
def print_maze(maze):
    total_rows = total_columns = len(maze)
    # Iterate over each cell in the maze
    for row in range(total_rows):
        for col in range(total_columns):
            # Check if current cell is the start point
            if (row == 0 and col == 0):
                print(colored(" S ","green","on_black"), end="")
            # Check if current cell is the end point
            elif (row == total_rows-1 and col == total_columns-1):
                print(colored(" E ","green","on_black"), end="")
            # Check if current cell is an empty space
            elif maze[row][col] == "◌":
                print(colored(" ◌ ","blue","on_white"), end="")
            # Check if current cell is a wall
            elif maze[row][col] == "▓":
                print(colored(" ▓ ","red","on_white"), end="")
            # Check if current cell is part of the path
            elif maze[row][col] == "◍":
                print(colored(" ◍ ","green","on_black"), end="")
        print()

# Function to find the path using Breadth-First Search (BFS)
def find_path(maze, start, goal):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible directions: up, down, left, right
    queue = deque([(start, [])])  # Initialize a deque with start position and empty path
    visited = set()  # Initialize an empty set to keep track of visited cells

    while queue:
        current, path = queue.popleft()  # Dequeue the first element
        x, y = current  # Extract x and y coordinates of the current position

        # If current position is the goal, return the path
        if current == goal:
            return path + [current]

        # If current position is already visited, skip it
        if current in visited:
            continue

        visited.add(current)  # Add current position to visited set

        # Explore each direction from the current position
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            # Check if the new position is within maze bounds and is an empty space, start, or end point
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and \
               (maze[new_x][new_y] == "◌" or maze[new_x][new_y] == "S" or maze[new_x][new_y] == "E"):
                queue.append(((new_x, new_y), path + [current]))  # Enqueue the new position with updated path

    return None  # Return None if no path is found

# Function to solve the maze using BFS
def solve_maze(maze):
    start_position = (0, 0)  # Start position of the maze
    end_position = (len(maze) - 1, len(maze[0]) - 1)  # End position of the maze

    # Find the path from start to end position
    path = find_path(maze, start_position, end_position)
    if path:
        # Mark the path in the maze
        for t in path:
            row, col = t[0], t[1]
            maze[row][col] = "◍"
        return True  # Path found
    return False  # No path found

# Main function to run the maze solver game
def main():
    print(colored("\nLet's Start the Maze Solver Game", "red", "on_black"))
    n = int(input("\nEnter the size of the maze (n*n) :-  "))  # Input maze size from user
    print()
    maze = generate_maze(n)  # Generate maze of size n
    print_maze(maze)  # Print the generated maze

    # Game loop
    while True:
        # Display menu options
        print("\n1. Print the Path ")
        print("2. Generate another Maze ")
        print("3. Exit ❌ the Game \n")
        
        # Get user choice
        players_choice = int(input("Enter Your Choice (1/2/3)❓❓:-  "))

        # Print the path in the maze
        if players_choice == 1:
            solution = solve_maze(maze)
            print()  # Print an empty line
            if solution:
                print(colored("Path Found", "green"))  # Print message if path found
                print()
                print_maze(maze)  # Print the maze with marked path
            else:
                print(colored("No path found", "red", "on_white"))  # Print message if no path found

        # Generate another maze
        elif players_choice == 2:
            n = int(input("\nEnter the size of the maze (n*n) :-  "))  # Input maze size from user
            maze = generate_maze(n)  # Generate a new maze
            print(colored("\nMaze Generated 👇", "blue"))  # Print message indicating maze generation
            print()
            print_maze(maze)  # Print the generated maze

        # Exit the game
        elif players_choice == 3:
            print("\nThank you for playing the Maze Solver Game.\n")  # Print farewell message
            break  # Exit the game loop

        else:
            players_choice = int(input("Enter Your Choice (1/2/3)❓❓:-  "))  # Prompt user for correct choice

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()