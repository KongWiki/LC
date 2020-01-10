"""
@time : 2020/1/5下午8:43
@Author: kongwiki
@File: 110.BalancedBinaryTree.py
@Email: kongwiki@163.com
"""
"""
给定一个二叉树 
判断其高度是否平衡（平衡二叉树的性质）
"""


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def isBalanced(self, root):
		"""
		判断是高度是否平衡
		:param root: 根节点
		:return: boolean
		"""
		if not root:
			return True
		left_height = self.height(root.left)
		right_height = self.height(root.right)
		if abs(left_height - right_height) <= 1:
			return self.isBalanced(root.left) and self.isBalanced(root.right)
		return False

	def height(self, root):
		if not root:
			return 0
		else:
			return max(self.height(root.left), self.height(root.right)) + 1


if __name__ == '__main__':
	input = [1, None, 2, None, 3]
	node_arr = []
	for i in input:
		tmp = TreeNode(i)
		node_arr.append(tmp)
	node_1 = node_arr[0]
	node_2 = node_arr[1]
	node_3 = node_arr[2]
	node_4 = node_arr[3]
	node_5 = node_arr[4]
	node_1.left = node_2
	node_1.right = node_3
	node_2.left = node_4
	node_2.right = node_5
	s = Solution()
	print(s.isBalanced(node_1))
