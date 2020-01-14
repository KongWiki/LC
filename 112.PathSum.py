"""
@time : 2020/1/14下午2:36
@Author: kongwiki
@File: 112.PathSum.py
@Email: kongwiki@163.com
"""
"""
计算是否存在路径上的数字之和等于所给的值
"""


class TreeNode:
	def __init__(self, x):
		self.left = None
		self.right = None
		self.val = x


class Solution:
	# def hasPathSum(self, root, sum):
	# 	"""
	# 	判断是否存在路径
	# 	:param root:
	# 	:return:
	# 	"""
	# 	stack = [root]
	# 	while stack:
	# 		current_node = stack.pop()
	# 		if current_node.left:
	# 			stack.append(current_node.left)
	# 		if current_node.right:
	# 			stack.append(current_node.right)
	def hasPathSum(self, root, sum):
		if not root:
			return False
		sum -= root.val
		if sum == 0 and root.left is None and root.right is None:
			return True
		return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)




