#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-20 17:30
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_153_查找旋转数组.py
# @Software: PyCharm

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        思路: 二分
        left/right/mid
        确定是否有顺序
        同首尾比较
        规约
        :param nums:
        :return:
        """
        left = 0
        right = len(nums)-1
        if len(nums) == 1:
            return nums[0]
        if nums[right] > nums[0]:
            return nums[0]

        while left <= right:
            mid = (left+right) // 2

            # 如果是<=进入到循环中
            # 返回数据中注意：包含最小值的各种情况都要考虑
            # 【最小值左边作为mid】 + 【最小值右边作为mid】
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid+1
            else:
                right = mid -1

