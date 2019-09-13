# -*- coding: utf-8 -*-
# @Time    : 2019-08-18 12:03
# @Author  : Frenkie
# @File    : leetcode_1.py


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        注意点：空间O(1) 且 必须原地修改输入数组
        => append, insert, remove first value, pop index, nums[0] = 1
        """
        # 时间 792ms
        if not nums:
            return 0

        # before_num = nums[0]
        # list remove, index-=1
        # for index, value in enumerate(nums[1:]):
        #     if value == before_num:
        #         nums.remove(value)
        #         index -= 1
        #     else:
        #         before_num = value
        # return len(nums)

        # 减少时间，减少enumerate和remove操作，减少了相应运行时间
        # 你不需要考虑数组中超出新长度后面的元素
        before_num = 0 # before_num后代表可替换的标志
        for i in range(1, len(nums)):
            if nums[before_num] != nums[i]:
                before_num += 1
                nums[before_num] = nums[i]

        return before_num+1

if __name__ == '__main__':
    nums = [1, 1, 2]
    s = Solution().removeDuplicates(nums)
    print(s)
    print(nums)


