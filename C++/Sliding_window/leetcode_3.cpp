//
// Created by Frankie on 2019/10/21.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // 设置window 和 窗口大小
        vector<int> window{};
        int res = 0;       // 窗口大小
        int left = 0;      // 窗口左边

        // 遍历字符串
        for (char &c : s) {
            // 字符串加到window中 append
            window.push_back(c);
            // 重复的话，删除元素直到不重复
            set<int> aset(window.begin(), window.end());
            if (window.size() != aset.size()) {
                window.erase(window.begin());
            }
        }
        // 返回res
        return window.size();
    }
};



int main() {
    Solution* s = new Solution();
    cout << s -> lengthOfLongestSubstring("abcabcdd") << endl;
    return 0;
}
