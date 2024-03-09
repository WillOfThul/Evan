
import random

class MazeSolver:
	
	def __init__(self, num_rows, num_cols):
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.path = []

	def draw_maze(self):
		c = self.num_cols
		r = self.num_rows
		self.maze = [[
			random.randint(1, 99)
			for _ in range(c)]
			for _ in range(r)]
		m = self.maze
		m[0][0] = "S"
		m[-1][-1] = "D"
	
	def print_maze(self):
		c = self.num_cols
		r = self.num_rows
		m = self.maze
		for i in range(r):
			line = ""
			line2 = ""
			for j in range(c):
				line += "%2s" % str(m[i][j])
				if j < c-1:
					if random.randint(1,3) <= 2:
						char = "→"
					else:
						char = "←"
					line += " " + char + " "
				if i < r-1:
					if random.randint(1,3) <= 2:
						char2 = "↓"
					else:
						char2 = "↑"
					line2 += "%2s" % char2
					line2 += "   " 
			print(line)
			print(line2)
	
	def solve_maze(self):
		self.path = []
		c = self.num_cols
		r = self.num_rows
		m = self.maze
		p = self.path
		def slave(q):
			for v in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
				w = (q[0] + v[0], q[1] + v[1])
				if w not in p and w[0] in range(r) and w[1] in range(c):
					if m[w[0]][w[1]] == 'D':
						return True
					elif m[w[0]][w[1]] != '#':
						p.append(w)
						if (slave(w)):
							return True
						assert(p.pop() == w)
		return slave((0, 0))
	
	def print_result(self):
		c = self.num_cols
		r = self.num_rows
		m = self.maze
		p = self.path
		for i in range(r):
			line = ""
			for j in range(c):
				line += "%4s" % ("+" if (i, j) in p else str(m[i][j]))
			print(line)
		print("The amount of coins collected:", sum([m[i][j] for (i, j) in self.path]))
