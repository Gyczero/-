#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 10:03 上午
# @Author  : Frankie
# @File    : leetcode_4_查找两个有序数组的中位数.py

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        思路:
        二分查找 => 框架
        :param nums1:
        :param nums2:
        :return:
        """

        mid1 = (len(nums1)-1)//2
        mid2 = (len(nums2)-1)//2

        while mid1<=len(nums1)-1 and  mid2<=len(nums2)-1:

            if nums1[mid1] < nums2[mid2]:
                mid1 = (len(nums1)-1+(mid1+1))//2
                mid2 = mid2 // 2
            elif nums1[mid1] > nums2[mid2]:
                mid2 = (len(nums2)-1+(mid2+1))//2
                mid1 = mid1 // 2
            else:
                return nums1[mid1]

        if mid1 > len(nums1)-1:
            return nums2[mid2]
        else:
            return nums1[mid1]


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 3], [2]))








