import unittest
from Binary_Search_Tree import Binary_Search_Tree


class BSTTester(unittest.TestCase):

	def setUp(self):

		self.__BST = Binary_Search_Tree()

	#Binary Search Tree Tests
	def test_height_empty(self):
		self.assertEqual(0, self.__BST.get_height())

	def test_height_one(self):
		self.__BST.insert_element(1)
		self.assertEqual(1, self.__BST.get_height())

	def test_height_four(self):
		self.__BST = Binary_Search_Tree()
		for i in [ 37, 10, 45, 42, 60, 52 ]:
			self.__BST.insert_element(i)
		self.assertEqual(4, self.__BST.get_height())

	def test_height_unchanged(self):
		self.__BST = Binary_Search_Tree()
		self.__BST.insert_element(37)
		self.__BST.insert_element(10)
		height1 = self.__BST.get_height()
		self.__BST.insert_element(45)
		height2 = self.__BST.get_height()
		return (height1 == height2)

	def test_height_changed(self):
		self.__BST = Binary_Search_Tree()
		self.__BST.insert_element(37)
		self.__BST.insert_element(10)
		self.__BST.insert_element(45)
		height1 = self.__BST.get_height()
		self.__BST.insert_element(42)
		height2 = self.__BST.get_height()
		return not(height1 != height2)

	def test_height_remove_height_unchanged(self):
		self.__BST = Binary_Search_Tree()
		for i in [ 37, 10, 45, 42, 60, 52, 67 ]:
			self.__BST.insert_element(i)
		self.__BST.remove_element(52)
		self.assertEqual(4, self.__BST.get_height())

	def test_height_remove_height_changed(self):
		self.__BST = Binary_Search_Tree()
		for i in [ 37, 10, 45, 42, 60, 52 ]:
			self.__BST.insert_element(i)
		self.__BST.remove_element(52)
		self.assertEqual(3, self.__BST.get_height())

	def test_breadth_first(self):
		self.__BST = Binary_Search_Tree()
		self.assertEqual("[ ]", self.__BST.breadth_first())
		for i in [ 37, 10, 45, 42, 60, 52 ]:
			self.__BST.insert_element(i)
		self.assertEqual("[ 37, 10, 45, 42, 60, 52 ]", self.__BST.breadth_first())

	def test_in_order(self):
		self.__BST = Binary_Search_Tree()
		self.assertEqual("[ ]", self.__BST.in_order())
		for i in [ 37, 10, 45, 42, 60, 52 ]:
			self.__BST.insert_element(i)
		self.assertEqual("[ 10, 37, 42, 45, 52, 60 ]", self.__BST.in_order())

	def test_pre_order(self):
		self.__BST = Binary_Search_Tree()
		self.assertEqual("[ ]", self.__BST.pre_order())
		for i in [ 37, 10, 45, 42, 60, 52 ]:
			self.__BST.insert_element(i)
		self.assertEqual("[ 37, 10, 45, 42, 60, 52 ]", self.__BST.pre_order())

	def test_post_order(self):
		self.__BST = Binary_Search_Tree()
		self.assertEqual("[ ]", self.__BST.post_order())
		for i in [ 37, 10, 45, 42, 60, 52 ]:
			self.__BST.insert_element(i)
		self.assertEqual("[ 10, 42, 52, 60, 45, 37 ]", self.__BST.post_order())

	def test_insert_existing(self):
		self.__BST = Binary_Search_Tree()
		self.__BST.insert_element(2)
		try:
			self.__BST.insert_element(2)
		except ValueError:
			return True

	def test_remove_nonexistent(self):
		self.__BST = Binary_Search_Tree()
		try:
			for i in [ 37, 10, 45, 42, 60, 52 ]:
				self.__BST.insert_element(i)
			self.__BST.remove_element(66)
		except ValueError:
			return True

	def test_remove_existent_one(self):
		self.__BST = Binary_Search_Tree()
		for i in [ 37, 10, 45, 42, 60, 52 ]:
			self.__BST.insert_element(i)
		self.__BST.remove_element(60)
		self.assertEqual("[ 37, 10, 45, 42, 52 ]", self.__BST.breadth_first())

	def test_remove_existent_none(self):
		self.__BST = Binary_Search_Tree()
		for i in [ 37, 10, 45, 42, 60, 52 ]:
			self.__BST.insert_element(i)
		self.__BST.remove_element(52)
		self.assertEqual("[ 37, 10, 45, 42, 60 ]", self.__BST.breadth_first())

	def test_remove_existent_two(self):
		self.__BST = Binary_Search_Tree()
		for i in [ 37, 10, 45, 42, 60, 52 ]:
			self.__BST.insert_element(i)
		self.__BST.remove_element(37)
		self.assertEqual("[ 42, 10, 45, 60, 52 ]", self.__BST.breadth_first())



if __name__ == '__main__':
	unittest.main(exit = False)
