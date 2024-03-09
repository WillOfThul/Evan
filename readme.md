
# Objectives
 - Manipulating two-dimensional lists
 - Using recursion to solve a problem
 - Review classes and inheritance

# Problem Specification
A Robot is waiting to be programmed to navigate a maze. The robot is required to start at the starting point (S) and find a path, if exist, to the destination (D). The location of the maze is either open (.) or blocked (#). If there is at least one path from S to D, the robot should tell the master and show a map, or otherwise just tell the master no path exists from S to D.

For this project, you will use recursion to solve mazes. First, you need to write a Python file that implements the maze solver that will run on the robot. The maze is a two-dimensional array/lists. The numbers of rows and columns are given by the user, and must be in the range of [5, 10] inclusively, without the number of rows being the same as that of columns. For example, if the number of rows is 6, then the number of column cannot be 6. The program needs to validate the input and ask for another input if invalid instead of terminating. Also, the program should print out corresponding reasons about why the input is invalid. For example, if the input is "a", the program should print "Sorry, the letter can't be used to set the number of rows. Please type in an integer within the range of [5, 10] inclusively". Once obtained, the number of rows and columns will be used to generate the maze. The maze consists of four symbols as below:

 - Number (e.g., "5") is the position where the robot is able to move. The number indicates the amount of coins that the Robot can collect at that position.
 - "#" is the position where a block is located.
 - "S" is the starting point. 
 - "D" is the destination.
 
The "S" is always at the top left, while the "D” is always at the bottom right of the maze. The "number" and "#" are randomly filled in the maze. The number should be within the range of [1, 100] inclusively, while the total number of "#" CANNOT be greater than 1/3 of the total positions of the maze. For example, for a 4x5 maze, the total number of "#" cannot exceed 6. Once the maze is drawn, the program should print it on the screen. The robot always starts from "S" and tries to find an available path to "D". The robot is able to move one step every time in one of the four directions (up, down, left and right) as long as there is no block ahead. The program MUST USE RECURSION to find the path. If the robot is not able to find a path, print the result accordingly. If the robot finds a path, then it needs to do two things:

 1. print out the maze with the path marked by "+".
 2. sum up all the numbers on this path and printed it out as the amount of coins found. *(Hint: you may need to cast the number to int in order to do arithmetic operation.)*

The program is also required to run the above process 3 times. Each time should be ordered accordingly. For example: Maze #1 Started... Maze #1 Result...

# Design Requirements
You are **REQUIRED** to use at two classes to finish the task, which `MazeInput` and `MazeSolver` classes. 

First think about the overall structure of your program. The basic structure has been provided for you in this assignment. However, you may have other attributes and/or methods in addition to those listed below:

# Main program (`main.py`):
A Python file that has a main method. The main method is implemented to create instances of classes `MazeInput` and `MazeSolver`, call proper methods in `MazeInput` class to get the maze size from the user and then create a new `MazeSolver` then call the proper methods in `MazeSolver` to start the maze. The whole process needs to repeat three times, with different mazes. 

## `class MazeInput` (in `MazeInput.py`):
 1. `promt_for_num_rows(self)`: This method asks for a number within the range of [5, 10] inclusively from the user as the number of rows. The program is responsible for validating the input and print corresponding reason if the input is not valid. 
 2. `promt_for_num_cols(self)`: This method asks a number within the range of [5, 10] inclusively from the user as the number of rows. This number CANNOT be the same as the number of rows denoted by parameter `num_rows`. The program is responsible for validating the input and print corresponding reason if the input is not valid.

## `class MazeSolver` (in `MazeSolver.py`):

 1. `draw_maze(self)`: Draw the maze (a 2D matrix) by randomly filling it with "#" (block) and number (e.g., "45"). Set the "S" (Starting point) to the top left, and "D" (Destination) to the bottom right. numbers are randomly generated within the range of [1, 100] inclusively, while the total number of "#" cannot exceed the 1/3 of the total size of the matrix. 
 2. `print_maze(self)`: The original maze is printed. Each column must be properly aligned.
 3. `solve_maze(self)`: This method is the core part to solve the maze. It tries to solve the maze using recursion. Returns `True` if there is at least one solution. Otherwise returns `False`.
 4. `print_result(self)`: If there is a solution, this method will be called to print out the maze with the path position replaced by "+". The amount of coins collected on the path is also calculated and printed in this method. Each column must be properly aligned.

# Example Output
See a sample report below. Use the EXACT format/wording/spacing/labeling/... shown in sample.  (use EXACT format – and NO HARDCODING of the data itself)

```tex
Enter number of rows in range [5, 10]: 1
Invalid input!
Enter number of rows in range [5, 10]: a
Input must be an integer!
Enter number of rows in range [5, 10]: 5
Enter number of columns in range [5, 10]: 5
This must be different from number of rows!
Enter number of columns in range [5, 10]: 6

******Maze #1******
Start drawing the maze...
The maze is as below:
   S  29   #  59  86
  92  43  80   #  17
   6  37  69  77   #
  59  67  56   3   #
  35  24  58  43  40
  54  28   #  92   D
Congratulations! I found a solution for this maze as below:
   S  29   #  59  86
   +  43  80   #  17
   +  37  69  77   #
   +  67  56   3   #
   +   +   +   +  40
   +   +   #   +   D
The amount of coins collected: 491

******Maze #2******
Start drawing the maze...
The maze is as below:
   S  86  56  51   9
  15  16  67  87  61
  73  80   5   #   #
  99  43   #  22  74
   7  93  61   #   9
  29  25  81  77   D
Congratulations! I found a solution for this maze as below:
   S  86  56  51   9
   +  16  67  87  61
   +  80   5   #   #
   +  43   #  22  74
   +  93  61   #   9
   +   +   +   +   D
The amount of coins collected: 406

******Maze #3******
Start drawing the maze...
The maze is as below:
   S   4   #  33  57
  65  47  87  44  62
  11  34  10  48  35
  93  33  37  33   #
 100  61  16   #  22
  79   #   #   #   D
Sorry, no solution can be found for this maze!
```

{try it | terminal}(./spoonfeed python3 main.py < example-input.txt)

# Additional Requirements  
## Coding Standards 
You must adhere to all conventions applicable to writing programs. This includes the use of white spaces and indentations for readability, the use of comments to explain the meaning of various methods and attributes, and the conventions for naming classes, variables, method parameters and methods.

NOTE: The penalty for late submissions as stated in the course syllabus will be applied in grading any assignment submitted late.


