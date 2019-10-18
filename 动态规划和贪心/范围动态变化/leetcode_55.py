#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 7:03 下午
# @Author  : Frankie
# @File    : leetcode_55.py

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        思路：
        1、求最大，遍历数组，求能到达的index数组
        2、遍历index数组，求最大，如果最大值大于长度，满足

        动态规划方程
        :param nums:
        :return:
        """
        # if not nums:
        #     return False
        #
        # # dp 初始化
        # dp = [False for i in nums]
        # dp[0] = True
        #
        # # dp主体
        # for i in range(1, len(nums)):
        #     for j in range(0, i):
        #         if dp[j] and j+nums[j] >= i:
        #             dp[i] = True
        #             break
        #
        # return dp[len(nums) - 1]

        """
        贪心算法：
        1、动态规划两层 => 贪心一层循环
        2、设置一个递增下标now，设置最大到达的地方，每次取最大
        3、递增下标就在最大的范围内尝试
        
        关键点：
        转化累积可以reach的范围 => 
        【当前pointer， 上限】 => 
        1、上限需要根据pointer更新，pointer增加 
        2、成功的边界条件
        pointer超过上限
        
        判断是否在范围中
        while now <= max_reach:
            max_reach = 根据now设置更新范围 比较函数
            now += 1
            成功的条件 return True的条件
        """
        if not nums:
            return False

        max_reach = 0
        now = 0
        while now <= max_reach:
            max_reach = max(now + nums[now], max_reach)
            now += 1
            if max_reach >= len(nums) - 1:
                return True
        return False
