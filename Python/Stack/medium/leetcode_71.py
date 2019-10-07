#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-07 11:27
# @Author  : Frenkie
# @Site    : 
# @File    : leetcode_71.py
# @Software: PyCharm

class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        思路：
        规则
        1、开始一个/
        2、中间有两个/，以一个/代替
        3、最后一个不能以/结尾
        4、必须最短的字符串 => 如果是./去掉，如果是../去掉前边的a/

        思路：栈的思想，后进先进行匹配，就近匹配, split / 后情况少了很多
        特殊情况处理：一直取上一级目录
        :param path:
        :return:
        """
        path_names = [""]
        paths = path.split("/")
        for apath in paths:
            if apath == "" or apath == ".":
                continue
            elif apath == '..':
                # 前一级目录，去掉最新的path
                # 特殊情况处理，一直取上一级的目录，返回当前目录
                if len(path_names) == 1:
                    continue
                else:
                    path_names.pop(-1)
            else:
                path_names.append(apath)

        # 特殊情况处理，如果当前path_names中只有空
        if len(path_names) == 1:
            result = "/"
        else:
            # 将path_names构成path
            result = "/".join(path_names)
        return result

if __name__ == '__main__':
    print(Solution().simplifyPath("/home/../../.."))






