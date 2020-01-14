"""
@time : 2020/1/14下午9:08
@Author: kongwiki
@File: 125.ValidPalindrome.py
@Email: kongwiki@163.com
"""
"""
回文字符串
"""


class Solution:
	def isPalindrome(self, s):
		"""
		判断是否是回文字符串
 		:param s:  给定的字符串
		:return: 布尔型
		"""
		alpha = [x for x in s.lower() if x.isalnum()]
		return alpha == alpha[::-1]
