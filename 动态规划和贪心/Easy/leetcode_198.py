#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-09-14 19:02
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_198.py
# @Software: PyCharm

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        思路:
        1、dp递推公式
        2、初始化
        3、循环
        :param nums:
        :return:
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        if nums[0] >= nums[1]:
            dp[1] = nums[0]
            last_is_rob = False
        else:
            dp[1] = nums[1]
            last_is_rob = True

        for i in range(2, len(nums)):

            # 如果最后一个被偷，判断
            if last_is_rob:
                sum1 = dp[i-1]
                sum2 = dp[i-2] + nums[i]
                if sum1 >= sum2:
                    dp[i] = sum1
                    last_is_rob = False
                else:
                    dp[i] = sum2
                    last_is_rob = True

            # 如果最后一个没被偷，直接偷这个
            else:
                dp[i] = dp[i-1] + nums[i]
                last_is_rob = True
        return dp[-1]

if __name__ == '__main__':
    print(Solution().rob([1,3,1,3,100]))
