#include <iostream>
#include <typeinfo>
using namespace std;

        class Solution {
        public:
            int strStr(string haystack, string needle) {
                // 【极限条件】如果needle为空，返回0
                if (needle.empty()) {
                    return 0;
                }

                if (haystack.empty()) {
                    return -1;
                }

        // 获取needle的长度
        int needle_len = needle.length();

        // 遍历haystack index - len
        // 取haystack index+len长度的string
        // 判断两个String是否相等，相等返回索引
        // .length()返回的类型默认是 unsigned int形式的
        for (int i = 0; i < int(haystack.length())-needle_len + 1; ++i) {
            string tem_str = haystack.substr(i, needle_len);
            if (tem_str == needle) {
                return i;
            }
        }
        return -1;
    }
};

int main() {
    // 新建Solution对象
    Solution *s = new Solution();
    // 调用strStr方法
    cout << s -> strStr("a", "a") << endl;
    return 0;
}
