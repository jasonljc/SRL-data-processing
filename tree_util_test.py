'''
Unit tests for tree_util.py.

'''

import unittest
import tree_util

class TreeUtilTest(unittest.TestCase):
	def setUp(self):
		self.root = tree_util.Node({'id':0, 'form':'improve'})
		self.root.add_children([
			tree_util.Node({'id':1, 'form':'economy'}),
			tree_util.Node({'id':2, 'form':'to'}),
			])
	
	def test_search_node(self):
		testcases = [('id', 2), ('form', 'economy'), ('pos', 1), ('form', 'one')]
		self.assertEqual(self.root.find_child('id', 2).label['id'], 2)
		self.assertEqual(self.root.find_child('form', 'economy').label['form'], 'economy')
		self.assertIsNone(self.root.find_child('pos', 1))
		self.assertIsNone(self.root.find_child('form', 'one'))

if __name__ == '__main__':
	unittest.main()