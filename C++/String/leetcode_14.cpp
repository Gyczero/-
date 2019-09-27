//
// Created by Frankie on 2019/9/25.
//

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        // 遍历第一个单词
        // 遍历整个list
        // 如果单词索引大于list的长度或有一个单词值同单词索引值不同，返回当前str
        // 极端情况，返回默认str
        string firstWord = strs[0];
        string *result = new string;

        for (int i = 0; i < int(firstWord.size()); ++i) {
            for (int j = 0; j < int(strs.size()); ++j) {
                if (firstWord[i] != strs[j][i] || i >= int(strs[j].length())) {
                    return *result;
                }
                // 一个string对象增加一个值
                result->insert()
            }
        }
        return *result;
    }
};

int main() {

    Solution *s = new Solution();
    // 新建一个vector类
    s -> longestCommonPrefix(new vector<>());
    return 0;
}