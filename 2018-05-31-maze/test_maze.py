import unittest
import maze

class CellTest(unittest.TestCase):

	def setUp(self):
		self.cell = maze.Cell(2,3)
	
	def test_init(self):
		self.assertEqual(self.cell.row, 2)
		self.assertEqual(self.cell.col, 3)
		self.assertFalse(self.cell.visited)


	def test_has_wall(self):
		self.assertTrue(self.cell.has_wall(maze.Cell.LEFT))
		
	def test_drill_wall(self):
		self.cell.drill_wall(maze.Cell.LEFT)
		self.assertFalse(self.cell.has_wall(maze.Cell.LEFT))

	def test_build_wall(self):
		self.cell.drill_wall(maze.Cell.LEFT)
		self.assertFalse(self.cell.has_wall(maze.Cell.LEFT))

		self.cell.build_wall(maze.Cell.LEFT)
		self.assertTrue(self.cell.has_wall(maze.Cell.LEFT))
	
class TestBoard(unittest.TestCase):

	def setUp(self):
		self.board = maze.Board(5, 6)
	
	def test_init(self):
		self.assertEqual(self.board.rows, 5)
		self.assertEqual(self.board.cols, 6)
		self.assertEqual(len(self.board.cells), 30)
	
	def test_get_cell(self):
		b = self.board
		c = b[1,4]
		self.assertEqual(c.row, 1)
		self.assertEqual(c.col, 4)

		

if __name__ == "__main__":
	unittest.main()

