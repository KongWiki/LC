"""
@time : 2020/1/13下午9:47
@Author: kongwiki
@File: 111.MinimumDepthOfBinaryTree.py
@Email: kongwiki@163.com
"""
"""
求树的最小高度
"""


class TreeNode:
	def __init__(self, x):
		self.left = None
		self.right = None
		self.value = x


class Solution:
	def minDepth(self, root):
		if not root:
			return 0
		depth, current_level = 0, [root]
		while current_level:
			depth += 1
			next_level = []
			for node in current_level:
				node_left, node_right = node.left, node.right
				if not node_left and not node_right:
					return depth
				if node_left:
					next_level.append(node_left)
				if node_right:
					next_level.append(node_right)
			current_level = next_level
		return depth


if __name__ == '__main__':
	nodes = [3, 9, 20, None, None, 15, 7]
	tree_nodes = [TreeNode(x) for x in nodes]
	tree_nodes[0].left = tree_nodes[1]
	tree_nodes[0].right = tree_nodes[2]
	tree_nodes[2].left = tree_nodes[5]
	tree_nodes[2].right = tree_nodes[6]
	s = Solution()
	print(s.minDepth(tree_nodes[0]))
