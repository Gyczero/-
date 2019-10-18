#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 10:04 下午
# @Author  : Frankie
# @File    : leetcode_33.py

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        时间复杂度必须是O(logN)级别
        logN 树 => 搜索 - 二分查找 => 二分查找的模板
        二分查找要求：部分有序数组
        一次排除一半或者一半以上元素的方法
        有了旋转点 => 搜索 - 二分查找 => 怎么找到旋转点
        => 中间middle
        1、如果这点比最后一个点小，并且比前一个点大 => 左边
        2、如果这点比最后一个点大，并且比前一个点大 => 右边
        3、如果这点比前一个点小，这点是旋转点
        修改规约方式 => 简单二分搜索
        模板：
        1、low, high, mid
        2、规约的设置
        3、最终结果的判断

        二分查找的思想是数据有序的，比较数据首尾和target的关系
        难点在于怎么判断每一部分的数据有序
        根据mid和left/right的值的大小判断
        left, right mid
        while left < right:
            if target > mid:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left] if xx else -1
        :param nums:
        :param target:
        :return:
        """
        # 1、极端情况
        size = len(nums)
        if size == 0:
            return -1

        left = 0
        right = len(nums) - 1
        # 2.1 left小于right开始

        while left < right:
            # 2.2 选择左中位数
            mid = (left + right) // 2

            # 2.3 如果中位数同target相等，返回中位数索引
            if nums[mid] == target:
                return mid

            # 2.4 二分精髓，判断是否有序，仅选择有序的进行对比
            if nums[mid] < nums[right]:
                # 右边有序
                # 2.5 仅对比两个数，判断是否在区间里，减少搜索空间 ！！！
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # 左边有序
                if nums[left] <= target <= nums[mid - 1]:
                    right = mid - 1
                else:
                    left = mid + 1

        # 2.6 最终结果，返回搜索得到的值
        return left if nums[left] == target else -1


if __name__ == '__main__':
    print(Solution().search([3, 1], 0))


