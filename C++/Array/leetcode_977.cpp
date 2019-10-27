//
// Created by Gyczerinvis on 2019-10-26.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        // 思路1：每个元素平方，排序 O(n^2)
//        for (auto& i: A) {
//            i = i*i;
//        }
//        sort(A.begin(), A.end());
//        return A;

        // 思路2：双指针
        // 观察：负数降序排列，正数升序排列
        // 时间复杂度O(n), 空间复杂度O(n)
        int flag = A.size();
        for (int j = 0; j < A.size(); ++j) {
            if (A[j] >= 0) {
                flag = j;
                break;
            }
        }
        int start = flag-1;
        for (auto &i: A) {
            i = i * i;
        }

        vector<int> ans;
        while(start >= 0 && flag < A.size()) {
            if (A[start] >= A[flag]) {
                ans.push_back(A[flag]);
                flag++;
            } else {
                ans.push_back(A[start]);
                start--;
            }
        }

        if (flag >= A.size()) {
            while (start >=0) {
                ans.push_back(A[start]);
                start--;
            }
        }
        else {
            while (flag < A.size()) {
                ans.push_back(A[flag]);
                flag++;
            }
        }
        return ans;
    }
};

int main() {
    Solution *s = new Solution();
    vector<int> test = {-4, -1, 0, 3, 10};
    s -> sortedSquares(test);
    return 0;
}