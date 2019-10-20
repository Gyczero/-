#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-20 18:19
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_162_寻找峰值.py
# @Software: PyCharm

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        关键点：
        题目假设nums[-1] = 负无穷
        如果nums[i] > nums[i+1]，那么i之前一定存在峰值
        为什么？
        为什么mid < mid+1，峰值一定在后边
        因为上坡，最后是负无穷
        为什么mid > mid+1, 峰值一定在左边
        因为nums[-1]为负无穷，上坡
        :param nums:
        :return:
        """
        left = 0
        right = len(nums)-1
        # 当这里是 < 时，允许中间right = mid，一个left = mid+1
        # 具体是否等于mid，根据判断的left,right而定
        # 判断是否等于target <=
        # 判断同i+1判断  <
        while left < right:
            # 因为这里取得是 【左位数】，所以只能同mid+1进行比较
            mid = (left + right) // 2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid
        # 最后返回left/right
        return left
