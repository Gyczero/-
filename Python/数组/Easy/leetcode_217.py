#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 9:27 PM
# @Author  : taicheng.guo
# @Site    : 
# @File    : leetcode_217.py
# @Software: PyCharm


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """

        :param nums:
        :return:
        """
        if len(nums) == len(list(set(nums))):
            return False
        else:
            return True