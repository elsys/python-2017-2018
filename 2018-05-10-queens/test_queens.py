import unittest

from queens import Board


class QueensTest(unittest.TestCase):
	
	def setUp(self):
		self.board = Board(4)
	
	def test_create(self):
		
		self.assertEqual(4, self.board.size)
		self.assertTrue(self.board.is_empty())

	def test_set_queen(self):
		
		with self.assertRaises(AssertionError):
			self.board.set_queen(5,0)
		with self.assertRaises(AssertionError):
			self.board.set_queen(0,6)

		self.board.set_queen(0,0)
		
		self.assertEqual(0, self.board.get_queen(0))
		self.assertIsNone(self.board.get_queen(1))

	def test_unset_queen(self):
		self.board.set_queen(0,0)
		self.assertFalse(self.board.is_empty())

		self.board.unset_queen(0)
		self.assertTrue(self.board.is_empty())

	def test_under_attack(self):
		self.board.set_queen(0,0)
		
		self.assertTrue(self.board.under_attack(1,0))
		self.assertTrue(self.board.under_attack(1,1))
		self.assertFalse(self.board.under_attack(1, 3))

		self.assertTrue(self.board.under_attack(0,1))
		

	def test_solve(self):
		
		self.board.solve()
		print(self.board.cells)
		### What to test here???
		
			
if __name__ == "__main__":
	unittest.main()

