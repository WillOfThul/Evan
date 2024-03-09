
import random

class MazeSolver:
	
	def __init__(self, num_rows, num_cols):
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.path = []

		self.l = open("log.txt", 'w')

	def draw_maze(self):
		c = self.num_cols
		r = self.num_rows
		self.maze = [
			[
			random.randint(1, 99)
			for _ in range(c)
			]
			for _ in range(r)
			]
		m = self.maze
		m[0][0] = "S"
		m[-1][-1] = "D"
		print(m)
	
	def print_maze(self):
		numCols = self.num_cols
		numRows = self.num_rows
		maze = self.maze
		newMaze = []
		for row in range(numRows):
			line = ""
			line2 = ""
			LRlist = []
			UDlist = []
			for col in range(numCols):
				line += "%2s" % str(maze[row][col])
				if col < numCols-1:
					if random.randint(1,3) <= 2:
						char = "→"
					else:
						char = "←"
					LRlist.append(char)
					line += " " + char + " "
				if row < numRows-1:
					if random.randint(1,3) <= 2:
						char2 = "↓"
					else:
						char2 = "↑"
					UDlist.append(char2)
					UDlist.append(None)
					line2 += "%2s" % char2
					line2 += "   " 
			print(line)
			print(line2)
			newMaze.append(line.split())
			if UDlist != []:
				UDlist.pop(-1)
				newMaze.append(UDlist)
		self.maze = newMaze
		print(self.maze)
	
	def solve_maze(self):
		self.path = []
		numCols = self.num_cols
		numRows = self.num_rows
		maze = self.maze
		path = self.path
		c = 0
		def slave(q, c):
			self.l.write(f'Run: {c}\n')
			self.l.write('For V---------------\n')
			for v in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
				self.l.write(f'Path: {path}\n')
				self.l.write(f'V: {v}\n')
				w = (q[0] + v[0], q[1] + v[1])
				self.l.write(f'W: {w}\n')
				if w not in path and w[0] in range(numRows) and w[1] in range(numCols):
					if maze[w[0]][w[1]] == 'D':
						return True
					elif maze[w[0]][w[1]] != '#':
						self.l.write(f'Path appending {w} (w)\n')
						path.append(w)
						if (slave(w, c)):
							self.l.write('Slave Done\n')
							return True
						
						assert(path.pop() == w)
			c += 1
			self.l.write('----------------------------------\n')
		return slave((0, 0), c)
	
	def check_surroundings(self, cord):
		x = cord[0]
		y = cord[1]
		maze = self.maze
		adjBook = {
			'u': [
				(0, 1),
				"↑"],
			'd': [
				(0, -1),
				"↓"],
			'l': [
				(1, 0),
				"←"],
			'r': [
				(-1, 0),
				"→"]
				}
		for word, direction in adjBook.items():
			newCord = (cord[0] + direction[0][0], cord[1] + direction[0][1])
			if maze[newCord[0]][newCord[1]] == direction[1]:
				direction[1] = True
			else:
				direction[1] = False
		return adjBook
		

	def solve_maze(self):
		self.path = []
		numCols = self.num_cols
		numRows = self.num_rows
		maze = self.maze
		path = self.path
		c = 0
		
		def slave(q, c):
			self.l.write(f'Run: {c}\n')
			self.l.write('For V---------------\n')
			for v in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
				self.l.write(f'Path: {path}\n')
				self.l.write(f'V: {v}\n')
				w = (q[0] + v[0], q[1] + v[1])
				self.l.write(f'W: {w}\n')
				if w not in path and w[0] in range(numRows) and w[1] in range(numCols):
					if maze[w[0]][w[1]] == 'D':
						return True
					elif maze[w[0]][w[1]] != '#':
						self.l.write(f'Path appending {w} (w)\n')
						path.append(w)
						if (slave(w, c)):
							self.l.write('Slave Done\n')
							return True
						
						assert(path.pop() == w)
			c += 1
			self.l.write('----------------------------------\n')
		return slave((0, 0), c)

	# def solve_maze(self, cord):
	# 	book = self.check_surroundings(cord)
	# 	def slave():

	# 		for key, item in book.items():
	# 			if item[1][1]:
	# 				newCord = (cord[0] + book.get(key)[0][0], cord[1] + book.get(key)[0][1])
					

		
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
