"""
@time : 2019/9/27下午9:38
@Author: kongwiki
@File: 019removeNthNodeFromEndofList.py
@Email: kongwiki@163.com
"""
"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list
becomes 1->2->3->5.
Note:

Given n will always be valid.

"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def myPrint(self):
		print(self.val)
		if self.next:
			self.next.myPrint()


class Solution:
	def removeNthFromEnd(self, head, n):
		if not head:
			return head
		# 设置头节点
		dummy = ListNode(-1)
		dummy.next = head
		prev = dummy
		curr = dummy
		print("当前的prev = {}, curr = {}".format(prev.val, curr.val))
		while prev and n >= 0:
			prev = prev.next
			print("n未结束当前的prev = {} curr = {} n = {}".format(prev.val, curr.val, n))
			n -= 1
		while prev:
			print("n之后当前的prev = {} curr = {}".format(prev.val, curr.val))
			prev = prev.next
			curr = curr.next
		curr.next = curr.next.next
		print("循环之后的curr={}".format(curr.val))
		return dummy.next


if __name__ == '__main__':
	n5 = ListNode(5)
	n4 = ListNode(4)
	n3 = ListNode(3)
	n2 = ListNode(2)
	n1 = ListNode(1)
	n1.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
	result = Solution().removeNthFromEnd(n1, 2)
	result.myPrint()