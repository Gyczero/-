# -*- coding: utf-8 -*-
# @Time    : 2019-08-18 12:03
# @Author  : Frenkie
# @File    : leetcode_1.py

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        时间复杂度: O(n)
        空间复杂度: O(n)
        :param nums:
        :param target:
        :return:
        """
        # for index1, i in enumerate(nums):
        #     for index2, j in enumerate(nums[index1+1: ]):
        #         if j == target - i:
        #             return [index1, index1+1+index2]

        """查找部分使用hash, O(n)方法,  空间O(n)"""
        tem_dict = {}
        for index, value in enumerate(nums):
            if value in tem_dict:
                return [tem_dict[value], index]
            else:
                tem_dict[target - value] = index


if __name__ == '__main__':

    s = Solution()
    print(s.twoSum([2,7,11,15], 9))


