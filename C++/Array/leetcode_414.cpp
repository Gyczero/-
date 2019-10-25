#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
    /*
     * 思路:
     * 1、循环
     * 2、记录第一大，第二大，第三大
     * 3、输出第三大
     */
public:
    int thirdMax(vector<int>& nums) {
        int first, second, third, tmp1, tmp2;

        // C++表示最小值
        first = second = third = tmp1 = tmp2 = INT_MIN;
        bool flag = false;

        // C++ iteration vector
        for (auto i: nums) {
            if (i == INT_MIN) {
                flag = true;
            }
            else if (i > first) {
                tmp1 = first;
                tmp2 = second;
                first = i;
                second = tmp1;
                third = tmp2;
            } else if (i > second && i != first) {
                tmp2 = second;
                second = i;
                third = tmp2;
            } else if (i >= third && i!= second && i!=first) {
                third = i;
            }
        }


        // 转为
        return third == INT_MIN? ((flag && second > third) ? third:first) : third;
        if (third == INT_MIN) {
            if (flag && second > third) {
                return third;
            }
            return first;
        } else {
            return third;
        }
}

};


int main() {
    Solution *s = new Solution();
    vector<int> test = {1, 2, 2, 5, 3, 5};
    cout << s -> thirdMax(test) << endl;
    return 0;
}