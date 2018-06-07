import turtle
import random

class Cell(object):
	STEP = 20

	DOWN = 0
	RIGHT = 1
	UP = 2
	LEFT = 3
	
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.walls = [True, True, True, True]
		self.visited = False
	
	@staticmethod
	def oposite_direction(direction):
		return (direction + 2) % 4
		
	def set_visited(self):
		self.visited = True
	
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

	def get_neighbour(self, cell, direction):
		assert Cell.DOWN <= direction <= Cell.LEFT
		if direction == Cell.LEFT:
			row = cell.row
			col = cell.col - 1
		elif direction == Cell.RIGHT:
			row = cell.row
			col = cell.col + 1
		elif direction == Cell.UP:
			row = cell.row + 1
			col = cell.col
		elif direction == Cell.DOWN:
			row = cell.row -1
			col = cell.col
		
		if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
			return None
		
		return self[row, col]

	def drill_wall(self, cell, direction):
		neighbour = self.get_neighbour(cell, direction)
		if neighbour is None:
			return None
		
		cell.drill_wall(direction)
		neighbour.drill_wall(Cell.oposite_direction(direction))
		
		return neighbour

	def get_unvisited_neighbours_directions(self, cell):
		neighbours = []
		for direction in range(4):
			n = self.get_neighbour(cell, direction)
			if n is None:
				continue
			if n.visited:
				continue
			neighbours.append(direction)
		
		return neighbours

	def generate(self, cell):
		cell.set_visited()
		
		while True:
			directions = self.get_unvisited_neighbours_directions(cell)
			if not directions:
				return
			direction = random.choice(directions)
			next = self.drill_wall(cell, direction)
			self.generate(next)


if __name__ == "__main__":
	
	turtle.speed(0)
	turtle.hideturtle()
	
	# c = Cell(2,3)
	# c.drill_wall(Cell.LEFT)
	# c.draw()
	b = Board(10, 10)
	start = b[0,1]
	b.generate(start)
	
	b.draw()

	input()
	
			
