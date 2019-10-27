//
// Created by Gyczerinvis on 2019-10-27.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
//        if (s.size() == 0) {
//            return;
//        }
//        // 双指针
//        vector<char>::iterator left = s.begin();
//        vector<char>::iterator right = s.end()-1;
//
//        while (left < right) {
//            char tmp = *left;
//            *left = *right;
//            *right = tmp;
//            left++;
//            right--;
//        }
        // 直接reverse
        reverse(s.begin(), s.end());

    }
};