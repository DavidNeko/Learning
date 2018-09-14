#coding = utf-8
"""
[Difficulty : Easy]

Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""



class Solution(object):

    def __init__(self):
        self.test_case_1 = [2,7,11,15]
        self.test_case_2 = [8, 6, 7, 4, 9, 3, 2]

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}

        for i, num in enumerate(nums):
            if target - num in num_dict and num_dict[target - num] != i:
                return [num_dict[target - num], i]
            else:
                num_dict[num] = i

    @staticmethod
    def test(self):
        print self.twoSum(self.test_case_1, 9)
        print self.twoSum(self.test_case_2, 10)
        print ""
