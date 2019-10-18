#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 3:08 下午
# @Author  : Frankie
# @File    : leetcode_34.py


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        思路：logN
        二分相等 => 小于target最大的数 + 大于target最小的数, 转换为 2logN
        :param nums:
        :param target:
        :return:
        """
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        left = 0
        right = len(nums) - 1

        # 找小于target最大的数
        while left < right:
            # 取左中位数
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if nums[mid + 1] == target:
                    left = mid
                    break
                else:
                    left = mid + 1

        # 整个二分查找返回的结果，如果【2，2】target = 2这种边界情况呢？
        low_target = left
        if nums[left] == target:
            low_target -= 1

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                if nums[mid - 1] == target:
                    left = mid
                    break
                else:
                    right = mid - 1
            else:
                left = mid + 1
        high_target = left
        if nums[high_target] == target:
            high_target += 1

        # 找不到
        if low_target >= high_target:
            return [-1, -1]
        return [low_target+1, high_target-1]


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))









