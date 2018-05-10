
class Board:
	
	def __init__(self, size):
		self.size=size
		self.cells = [ None for _ in range(self.size)]
	
	def is_empty(self):
		checks = [c is None for c in self.cells]
		return all(checks)

	def set_queen(self, col, row):
		assert 0 <= col < self.size
		assert 0 <= row < self.size
		self.cells[col] = row

	def get_queen(self, col):
		assert 0 <= col < self.size
		return self.cells[col]

	def unset_queen(self, col):
		assert 0 <= col < self.size
		self.cells[col] = None
	
	def under_attack(self, col, row):
		assert 0 <= col < self.size
		assert 0 <= row < self.size

		if self.cells[col] is not None:
			return True

		for r in self.cells:
			if r is not None and r == row:
				return True
		
		for c in range(self.size):
			r = self.cells[c]
			if r is None:
				continue
			if abs(row-r) == abs(col-c):
				return True
		return False


	def solve(self, col=0):
		if col == self.size:
			return True

		for row in range(self.size):
			if not self.under_attack(col, row):
				self.set_queen(col, row)
				if self.solve(col+1):
					return True
				self.unset_queen(col)

		return False

	def pretty_print(self):
		"""
		+-+-+-+-+
		|Q| | | |
		+-+-+-+-+
		| | |Q| |
		+-+-+-+-+
		"""
		pass

	def draw(self):
		"""
		turtle graphics
		"""
		pass


if __name__ == "__main__":

	board = Board(8)
	board.solve()
	
	print(board.cells)


