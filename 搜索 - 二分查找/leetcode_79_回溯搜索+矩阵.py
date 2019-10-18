#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 11:58 上午
# @Author  : Frankie
# @File    : leetcode_79_回溯搜索+矩阵.py


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        :param board:
        :param word:
        :return:
        """
        if len(board) == 0 or len(board[0]) == 0:
            return False

        choose_list = range(len(board) * len(board[0]))
        if self._dfs(board, "", word, choose_list, []):
            return True
        return False

    def _dfs(self, board, path, word, choose, ban_idxs):
        """
        nums, choose, path, res, 终止条件
        矩阵 = list
        row = idx // n
        col = idx % n

        start = 可以choose的index
        ban_idx：同一个单元格内的字母不允许重复使用
        矩阵主要事项：
        1、矩阵边上的值与相邻，比如0列的数据，左边相邻的并不是list的值-1；-1列的数据，右边相邻的并不是list的值+1
        2、矩阵 = list index的相互转换
        :return:
        """
        ncol = len(board[0])
        nrow = len(board)
        nums = nrow * ncol

        if path != word[:len(path)]:
            return False
        elif path == word:
            return True

        for idx in choose:
            # 根据这次选择，设置下一次的choose列表
            next_choose = []
            if idx - 1 >= 0 and idx-1 not in  ban_idxs and idx%ncol != 0:
                next_choose.append(idx - 1)
            if idx + 1 <= nums - 1 and idx+1 not in ban_idxs and (idx+1)%ncol != 0:
                next_choose.append(idx + 1)
            if idx - ncol >= 0 and idx-ncol not in ban_idxs:
                next_choose.append(idx - ncol)
            if idx + ncol <= nums - 1 and idx + ncol not in ban_idxs:
                next_choose.append(idx + ncol)
            # 根据这次choose增加path
            path += board[idx // ncol][idx % ncol]
            ban_idxs.append(idx)

            if self._dfs(board, path, word, next_choose, ban_idxs):
                return True
            else:
                path = path[:-1]
                ban_idxs.pop(-1)
                continue
        return False

if __name__ == '__main__':
    print(Solution().exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCED"))
