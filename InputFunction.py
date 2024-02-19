import os
os.system('color')
from termcolor import colored


def main():
    
    print(colored("\nLet's Start the Maze Solver Game","red","on_white"))
    n = int(input("\nEnter the size of the maze (n*n) :-  "))
    print()
    maze = generate_maze(n) 
    print_maze(maze)     
    # print(maze)
    while True:
    
        print("\n1. Print the Path ")
        print("2. Generate another Maze ")
        print("3. Exit❌ the Game \n")
        
        players_choice=int(input("Enter Your Choice (1/2/3):-  "))
        
        if players_choice==1:
            
            solution = solve_maze(maze)
            # print(maze)
            
            if solution:
                print(colored("\nPath Found \n","green","on_white"))
                print_maze(maze)
            else:
                print(colored("\nNo path found \n","red","on_white"))        
            
        elif players_choice==2:
            n = int(input("\nEnter the size of the maze (n*n) :-  "))
            maze = generate_maze(n)
        
            # print(maze)
        
            print(colored("\nMaze Generated 👇","blue"))
            print()
            print_maze(maze)

            
        elif players_choice == 3:
            
            print("\nThank you for playing the Maze Solver Game.\n")
            break
        
        else:
            players_choice=int(input("Enter Your Choice (1/2/3)❓❓:-  "))
            
if __name__ == "_main_":
    main()