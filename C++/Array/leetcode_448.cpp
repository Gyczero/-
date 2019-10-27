//
// Created by Gyczerinvis on 2019-10-27.
//

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    // 类似bitset的思想
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> res;
        int nums_len = nums.size();
        for (int i = 0; i <= nums_len; ++i) {
            res.push_back(1);
        }

        for (auto i: nums) {
            if (res[i] == 1) {
                res[i] = 0;
            }
        }

        int start = 0;
        for (int i = 0; i <= nums_len; ++i) {
            if (res[i] == 1) {
                res[start] = i;
                start++;
            }
        }

        int delta = nums_len - start;
        while (delta > 0) {
            res.erase(res.end()-1);
            delta--;
        }
        return res;
    }
};

int main() {
    Solution *s = new Solution();
    return 0;
}