#!/usr/bin/python3

from MazeSolver import MazeSolver
from MazeInput import MazeInput
import random

def main():
	mi = MazeInput()
	mi.promt_for_seed()
	mi.promt_for_num_rows()
	mi.promt_for_num_cols()
	ms = MazeSolver(mi.num_rows, mi.num_cols)
	random.seed(mi.maze_seed)
	for i in range(1, 3 + 1):
		print("\n******Maze #%i******" % i)
		print("Start drawing the maze...")
		ms.draw_maze()
		print("The maze is as below:")
		ms.print_maze()
		if (ms.solve_maze()):
			print("Congratulations! I found a solution for this maze as below:")
			ms.print_result()
		else:
			print("Sorry, no solution can be found for this maze!")
	ms.l.close()

main()
