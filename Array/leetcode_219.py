#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 9:30 PM
# @Author  : taicheng.guo
# @Site    : 
# @File    : leetcode_219.py
# @Software: PyCharm


from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        注意点：
        1、时间复杂度O(nk)
        2、借助hash, 时间复杂度O(n)
        :param nums:
        :param k:
        :return:
        """
        index_min_dict = {}
        is_match = False

        for i in range(len(nums)):
            if nums[i] in index_min_dict.keys():
                if i - index_min_dict[nums[i]] <= k:
                    return True
                else:
                    index_min_dict[nums[i]] = i
            else:
                index_min_dict[nums[i]] = i

        return is_match