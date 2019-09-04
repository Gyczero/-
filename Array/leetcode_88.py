#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 9:56 PM
# @Author  : taicheng.guo
# @Site    : 
# @File    : leetcode_88.py
# @Software: PyCharm

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        注意点：
        1、list inplace排序: nums1.sort(reverse=False)
        """
        nums1[m:] = nums2
        nums1.sort(reverse=False)


if __name__ == '__main__':

    s = Solution()
    nums1 = [1,2,3,0,0,0]
    s.merge(nums1, 3, [2,5,6], 3)
    print(nums1)