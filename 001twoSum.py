"""
@author：KongWeiKun
@file: twoSum.py
@time: 18-3-13 下午3:14
@contact: 836242657@qq.com
"""


class Solution:
	@staticmethod
	def twoSum(nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		dic = {}
		for index, num in enumerate(nums):
			if num in dic:
				return [dic[num], index]
			dic[target - num] = index


if __name__ == '__main__':
	nums = [2, 7, 11, 15]
	target = 9
	print(Solution.twoSum(nums, target))
	# assert (Solution().twoSum(nums,target))
	# nums = [3,2,4]
	# target = 6
	# assert (Solution().twoSum(nums,target) == [1,2])
