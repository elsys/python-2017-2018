import turtle


class Cell(object):
	STEP = 10

	DOWN = 0
	RIGHT = 1
	UP = 2
	LEFT = 3
	
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.walls = [True, True, True, True]
		self.visited = False
	
	def has_wall(self, direction):
		assert self.DOWN <= direction <= self.LEFT
		return self.walls[direction]

	def drill_wall(self, direction):
		assert self.DOWN <= direction <= self.LEFT
		self.walls[direction] = False
	
	def build_wall(self, direction):
		assert self.DOWN <= direction <= self.LEFT
		self.walls[direction] = True
		
	def draw(self):
		turtle.penup()
		turtle.goto(
			self.col * self.STEP,
			self.row * self.STEP)
		turtle.setheading(0)
		for direction in range(4):
			if self.has_wall(direction):
				turtle.pendown()
			else:
				turtle.penup()
			turtle.forward(self.STEP)
			turtle.left(90)
		turtle.penup()


class Board(object):
	
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		
		self.cells = [
			Cell(i // self.cols, i % self.cols)
			for i in range(self.rows* self.cols)
		]
	
	def __getitem__(self, index):
		# print("index:", index)
		row, col = index
		assert 0 <= row < self.rows
		assert 0 <= col < self.cols
		return self.cells[row*self.cols + col]

	def draw(self):
		for c in self.cells:
			c.draw()


if __name__ == "__main__":
	
	turtle.speed(0)
	turtle.hideturtle()
	
	# c = Cell(2,3)
	# c.drill_wall(Cell.LEFT)
	# c.draw()
	b = Board(10, 20)
	b.draw()

	input()
	
			
