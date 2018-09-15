# coding = utf-8
"""
Given a non-empty array of integers,
every element appears twice except for one.
Find that single one.

Note:

Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:
    Input: [2,2,1]
    Output: 1

Example 2:
    Input: [4,1,2,1,2]
    Output: 4

"""

class Solution(object):

    def __init__(self):

    def SingleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_dict = {}

        # set num_dict
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1

        # iterate num_dict
        for key, val in num_dict.iteritems():
            if val == 1:
                return key


    def SingleNumber_s2(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        bit operate
        use xor
        """

        res = 0
        for num in nums:
            res ^= num
        return res
