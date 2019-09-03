#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-03 22:12
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_53.py
# @Software: PyCharm

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        注意点：递推 !!!
        1、maxSub[i] = max(maxEnd[i], maxSub[i-1]) => maxSub[i-1] = max(...)
        2、maxSub[i] = max(maxEnd[i], maxEnd[i-1], ...)
        3、maxEnd[i] = max(maxEnd[i-1]+nums[i], nums[i])
        :param nums:
        :return:
        """
        maxSum = [i for i in nums]
        for i in range(1, len(nums)):
            maxSum[i] = max(maxSum[i-1] + maxSum[i], maxSum[i])
        return max(maxSum)




