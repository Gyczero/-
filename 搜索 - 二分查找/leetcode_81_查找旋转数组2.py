#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 10:19 上午
# @Author  : Frankie
# @File    : leetcode_81_查找旋转数组2.py

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        思路：
        1、二分
        注意：如果无法判断哪边有序，可以使left+=1 or right-=1
        :param nums:
        :param target:
        :return:
        """
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right - left) // 2
            # 计算mid -> 判断是否有序 -> 比较 -> 规约
            # 有序的旋转数组
            # 特殊情况
            if nums[mid] == target:
                return True

            # 如果中间和左右相等时，无法区分哪边有序，仅-=1/+=1
            # 相当于去掉了一个排除项，最坏情况下时间复杂度O(N)
            # bad case like: [1, 1, 3, 1] 和 [3, 1, 1]
            elif nums[mid] == nums[left]:
                left +=1
                continue
            elif nums[mid] == nums[right]:
                right -=1
                continue

            # 按照照常的二分查找
            elif nums[mid] < nums[right]:
                if target > nums[right] or target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[mid] > nums[right]:
                # 左边有序
                if target < nums[left] or target > nums[mid]:
                    left = mid+1
                else:
                    right = mid - 1

        return False

if __name__ == '__main__':
    print(Solution().search([3, 1, 1], 3))

