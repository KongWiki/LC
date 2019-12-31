"""
@time : 2019/12/29下午9:17
@Author: kongwiki
@File: 108.ConvertSortedArrayToBinarySearchTree.py
@Email: kongwiki@163.com
"""
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def sortedArrayToBST(self, nums):
		return self._sortedArrayToBST(nums, 0, len(nums))

	def _sortedArrayToBST(self, nums, left, right):
		if left == right:
			return None

		mid = (left + right) >> 1
		root = TreeNode(nums[mid])
		root.left = self._sortedArrayToBST(nums, left, mid)
		root.right = self._sortedArrayToBST(nums, mid + 1, right)
		return root


