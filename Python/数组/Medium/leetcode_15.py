#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-11 21:47
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_15.py
# @Software: PyCharm

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        思路：
        1、a+b+c=0
        2、当一个数确定，转化为数组中寻找两个数的和为-k
        3、排序+双指针
        :param nums:
        :return:
        """
        nums.sort(reverse=False)
        reuslt_list = []
        # 防止重复，固定第一个值
        # i和j加起来等于一个非负数
        for index in range(len(nums)-2):
            i, j = index+1, len(nums)-1

            # 防止重复
            if nums[index] > 0:
                continue
            # 防止重复, 先匹配最前边的，后跳过后边的
            if index>0 and nums[index] == nums[index-1]:
                continue

            while(i < j):
                sumij = nums[i] + nums[j]
                if sumij == -nums[index]:
                    reuslt_list.append([nums[index], nums[i], nums[j]])
                    i+=1
                    j-=1
                    while i<j and nums[i] == nums[i-1]: i+=1
                    while i<j and nums[j] == nums[j+1]: j-=1
                elif sumij > -nums[index]:
                    j-=1
                    while i<j and nums[j] == nums[j+1]: j-=1
                else:
                    i+=1
                    while i<j and nums[i] == nums[i-1]: i+=1
        return reuslt_list


if __name__ == '__main__':

    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))


