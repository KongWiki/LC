"""
@time : 2019/9/17下午4:43
@Author: kongwiki
@File: 002addTwoNumbers.py
@Email: kongwiki@163.com
"""

"""

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes 
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
 except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def addTwoNumbers(self, l1, l2):
		"""
		:param l1: ListNode
		:param l2: ListNode
		:return: ListNOde
		"""
		temp = ListNode(0)
		l3 = temp
		carry = 0
		while l1 or l2 or carry:
			add, carry = carry, 0
			if l1:
				add += l1.val
				l1 = l1.next
			if l2:
				add += l2.val
				l2 = l2.next
			if add > 9:
				add -= 10
				carry = 1
			l3.next = ListNode(add)
			l3 = l3.next

	def addTwoNumbersII(self, l1, l2):
		_i = 0
		head = None
		tail = None
		while l1 or l2:
			i = _i + (l1.val if l1 is not None else 0) \
				+ (l2.val if l2 is not None else 0)
			i, _i = i % 10, i // 10
			node = ListNode(i)
			if head is None:
				head = node
				tail = node
			else:
				tail.next = node
				tail = node
			l1 = l1.next if l1 is not None else None
			l2 = l2.next if l2 is not None else None
		if _i != 0:
			node = ListNode(_i)
			tail.next = node
		return head


if __name__ == '__main__':
	l1 = ListNode(9)
	l1.next = ListNode(8)
	l2 = ListNode(1)
	l2.next = ListNode(9)
	Solution().addTwoNumbers(l1, l2)
