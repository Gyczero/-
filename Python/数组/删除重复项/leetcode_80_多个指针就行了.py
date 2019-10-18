#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 4:59 下午
# @Author  : Frankie
# @File    : leetcode_80_多个指针就行了.py


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        数组inplace删除重复项
        指针，多个指针
        :param nums:
        :return:
        """
        assign = 1
        pointer = 1
        more_than_two = False

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if more_than_two:
                    pointer += 1
                else:
                    more_than_two = True
                    nums[assign] = nums[pointer]
                    assign +=1
                    pointer += 1
            else:
                more_than_two = False
                nums[assign] = nums[pointer]
                assign += 1
                pointer += 1
        return assign
