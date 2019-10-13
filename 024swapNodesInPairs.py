"""
@time : 2019/10/13下午8:32
@Author: kongwiki
@File: 024swapNodesInPairs.py
@Email: kongwiki@163.com
"""
"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def myprint(self):
		print(self.val)
		if self.next:
			self.next.myprint()

class Solution:
	def swapPairs(self, head):
		if not head:
			return
		dummy = ListNode(-1)
		dummy.next = head
		curr = dummy
		while(curr.next !=None and curr.next.next!=None):
			#
			tmp = curr.next.next
			# 两节点之间的交换
			curr.next.next = tmp.next
			tmp.next = curr.next
			curr.next = tmp
			# 下一个起始点
			curr = tmp.next

		head = dummy.next
		return head


if __name__ == '__main__':
	n1 = ListNode(1)
	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)
	n1.next = n2
	n2.next = n3
	n3.next = n4
	s = Solution()
	s.swapPairs(n1).myprint()
