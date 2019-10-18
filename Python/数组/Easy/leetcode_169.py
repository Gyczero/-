#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 23:30
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_169.py
# @Software: PyCharm

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        注意点：
        1、暴力、哈希、排序
        :param nums:
        :return:
        """

        # 排序 O(nlogn)
        # return sorted(nums)[len(nums) // 2]

        # 哈希 O(n)
        num_dict = {}
        for i in nums:
            num_dict[i] = num_dict.get(i, 0) + 1
            if num_dict[i] > len(nums) // 2:
                return i


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([3,2,3]))