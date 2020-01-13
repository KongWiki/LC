"""
@time : 2020/1/13下午9:24
@Author: kongwiki
@File: 104.MaximumDepthOfBinaryTree.py
@Email: kongwiki@163.com
"""
"""
寻找树的最大高度
"""


class TreeNode:
	def __init__(self, x):
		self.left = None
		self.right = None
		self.value = x


class Solution:
	def maxDepth(self, root):
		if not root:
			return 0
		left_height = self.maxDepth(root.left)
		right_hegiht = self.maxDepth(root.right)
		return max(left_height, right_hegiht) + 1

	def supper_maxDepth(self, root):
		if not root:
			return 0
		stack = [(root, 1)]
		depth = 1
		while stack:
			current_node, height = stack.pop()
			depth = max(depth, height)
			if current_node.left:
				stack.append([current_node.left, height+1])
			if current_node.right:
				stack.append([current_node.right, height+1])
		return depth


if __name__ == '__main__':
	nodes = [3,9,20,None, None, 15,7]
	tree_nodes = [TreeNode(x) for x in nodes]
	tree_nodes[0].left = tree_nodes[1]
	tree_nodes[0].right = tree_nodes[2]
	tree_nodes[2].left = tree_nodes[5]
	tree_nodes[2].right = tree_nodes[6]
	s = Solution()
	print(s.maxDepth(tree_nodes[0]))

