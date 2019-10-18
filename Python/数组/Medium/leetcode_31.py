#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 5:54 下午
# @Author  : Frankie
# @File    : leetcode_31.py

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        12345 -> 12354 -> 12435 -> 12453 -> 12534

        把一定情况的全排列顺序写出来，观察：
        1、从后往前，找出第一次出现的正序对k, k+1
        2、因为k+1之后是逆序，找到5之后比k高的最后一个数，同5交换
        3、交换后将k之后数据翻转

        之后思考方法：记住全排列，画出多个序列，观察
        记忆：全排列的下一个思路
        """
        for i in range(-1, -len(nums), -1):
            if nums[i] > nums[i-1]:

                latest_bigger = 0
                for j in range(i, 0, 1):
                    if nums[j] <= nums[i-1]:
                        latest_bigger = j
                        break
                latest_bigger -= 1

                tem = nums[i-1]
                nums[i-1] = nums[latest_bigger]
                nums[latest_bigger] = tem

                nums[i:] = nums[i:][::-1]
                return

        nums.sort()
        return

if __name__ == '__main__':
    nums = [1, 5, 1]
    Solution().nextPermutation(nums)
    print(nums)





