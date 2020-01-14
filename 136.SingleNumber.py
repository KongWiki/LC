"""
@time : 2020/1/14下午10:13
@Author: kongwiki
@File: 136.SingleNumber.py
@Email: kongwiki@163.com
"""
"""
寻找单个的元素
"""


class Solution:
	def singleNumber(self, nums):
		"""

		:param nums: a list
		:return:
		"""
		nums_dict = {}
		for i in nums:
			if i in nums_dict:
				nums_dict[i] += 1
			else:
				nums_dict[i] = 1
		return sorted(nums_dict.items(), key=lambda x: x[1], reverse=False)[0][0]


if __name__ == '__main__':
	a = [4, 1, 2, 1, 2]
	s = Solution()
	number = s.singleNumber(a)
	print(number)
	print(1^5)