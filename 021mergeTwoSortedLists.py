"""
@time : 2019/10/8下午8:11
@Author: kongwiki
@File: 021mergeTwoSortedLists.py
@Email: kongwiki@163.com
"""
"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

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
	def mergeTwoLists(self, l1, l2):
		if not l1 or not l2:
			return l1 or l2
		head = cur = ListNode(0)
		while l1 and l2:
			if l1.val < l2.val:
				cur.next = l1
				l1 = l1.next
			else:
				cur.next = l2
				l2 = l2.next
			cur = cur.next
		cur.next = l1 or l2
		return head.next


if __name__ == '__main__':
	s = Solution()
	n6 = ListNode(4)
	n5 = ListNode(3)
	n4 = ListNode(1)
	n3 = ListNode(4)
	n2 = ListNode(2)
	n1 = ListNode(1)
	n1.next = n2
	n2.next = n3

	n4.next = n5
	n5.next = n6

	# n1.myprint()
	# print('\n')
	# n4.myprint()
	s.mergeTwoLists(n1, n4).myprint()
