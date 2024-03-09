def safe_int(x):
	try:
		return int(x)
	except:
		return None

class MazeInput:
	
	def __init__(self):
		self.num_rows = None
		self.num_cols = None
		self.maze_seed = None

	def promt_for_num_rows(self):
		while self.num_rows is None:
			text = input("Enter number of rows in range [5, 10]: ")

			# if isinstance(text, int):


			integer = safe_int(text)
			if integer is None:
				print("Input must be an integer!")
			elif integer not in range(5, 10 + 1):
				print("Invalid input!")
			elif integer == self.num_cols:
				print("This must be different from number of columns!")
			else:
				self.num_rows = integer
	
	def promt_for_num_cols(self):
		while self.num_cols is None:
			text = input("Enter number of columns in range [5, 10]: ")
			integer = safe_int(text)
			if integer is None:
				print("Input must be an integer!")
			elif integer not in range(5, 10 + 1):
				print("Invalid input!")
			elif integer == self.num_rows:
				print("This must be different from number of rows!")
			else:
				self.num_cols = integer
	
	def promt_for_seed(self):
		while self.maze_seed is None:
			text = input("Enter seed for maze generation: ")
			integer = safe_int(text)
			if integer is None:
				print("Input must be an integer!")
			else:
				self.maze_seed = integer
