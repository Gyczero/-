//
// Created by Frankie on 2019/10/28.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        if (s.size() == 0) {
            return 0;
        }

        int right = s.size()-1;
        int res = 0;

        while (right >= 0) {
            if (s[right] == ' ') {
                if (res) {
                    return res;
                }
            } else {
                res++;
            }
            right--;
        }
        return res;
    }
};

int main() {

    return 0;
}