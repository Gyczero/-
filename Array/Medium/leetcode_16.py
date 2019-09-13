#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-13 17:16
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_16.py
# @Software: PyCharm

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        思路：
        1、三重循环: O(n^3)
        2、排序+双指针: 两重循环 => 每组输入只存在唯一答案
        :param nums:
        :param target:
        :return:
        """
        min_delta = 9999999
        # 从小到大排序
        nums.sort(reverse=False)

        for index in range(len(nums)-2):
            i = index+1
            j = len(nums)-1
            value1 = nums[index]

            # 双指针
            while(i < j):
                value_sum = value1 + nums[i] + nums[j]
                delta = abs(target - value_sum)

                if delta < min_delta:
                    min_delta = delta
                    nearest_sum = value_sum

                if value_sum > target:
                    j-=1
                else:
                    i+=1

        return nearest_sum


if __name__ == '__main__':

    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))




