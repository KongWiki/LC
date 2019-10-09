"""
@time : 2019/10/9下午8:28
@Author: kongwiki
@File: 023mergeKSortedLists.py
@Email: kongwiki@163.com
"""
"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
import heapq


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def myprint(self):
		print(self.val)
		if self.next:
			self.next.myprint()


class Solution:
	def mergetKSortedLists(self, lists):
		head = temp = ListNode(-1)
		heap = []

		for nodes in lists:
			if nodes:
				heapq.heappush(heap, (nodes.val, nodes))

		while heap:
			# 弹出最小元素
			smallestNode = heapq.heappop(heap)[1]
			temp.next = smallestNode
			temp = temp.next

			if smallestNode.next:
				heapq.heappush(heap, (smallestNode.next.val, smallestNode.next))
		return head.next


	def mergeKSortedLists(self, lists):
		dummy = curr = ListNode(-1)
		all_nodes = []
		for node in lists:
			while node:
				all_nodes.append(node.val)
				node = node.next
		print(all_nodes)
		all_nodes.sort()
		for val in all_nodes:
			curr.next = ListNode(val)
			curr = curr.next
		return dummy.next



if __name__ == '__main__':
	n1 = ListNode(1)
	n4 = ListNode(4)
	n5 = ListNode(5)
	n1.next = n4
	n4.next = n5

	n12 = ListNode(1)
	n3 = ListNode(3)
	n42 = ListNode(4)
	n12.next = n3
	n3.next = n42

	n2 = ListNode(2)
	n6 = ListNode(6)
	n2.next = n6

	print(n1.myprint())
	print("\n")
	print(n12.myprint())
	print("\n")
	print(n2.myprint())

	s = Solution()
	lists = []
	lists.append(n1)
	lists.append(n12)
	lists.append(n2)
	s.mergeKSortedLists(lists)