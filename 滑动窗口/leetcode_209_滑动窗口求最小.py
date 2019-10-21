#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 1:30 下午
# @Author  : Frankie
# @File    : leetcode_209_滑动窗口求最小.py


from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        思路: 滑动窗口

        窗口list
        一层循环
        判断：
        原始滑动窗口
        for 每个元素
            窗口数值+
            while cur >= s:
            减少窗口大小
            res = min(res, right-left+1)
            cur -= nums[left]
            left += 1
        返回最小的窗口值

        改进滑动窗口
        1、什么时候窗口保持大小不变
        2、什么时候窗口进行规约，减少数量（窗口进行扩大，增加数量）
        返回窗口大小

        :param s:
        :param nums:
        :return:
        """

        # 滑动窗口模板
        left = 0    # 窗口左侧
        cur = 0     # 窗口当前值
        res = float("inf")  # 窗口大小
        if sum(nums) < s and not nums:
            return 0

        for right in range(len(nums)):
            cur += nums[right]  # 窗口当前值增加
            while cur >= s:     # 判断条件，是否需要进行窗口放缩
                res = min(res, right-left+1)   # 是否需要记录
                cur -= nums[left]
                left += 1

        return res if res != float("inf") else 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8]))


