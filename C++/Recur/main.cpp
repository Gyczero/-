#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int fib(int N) {
        vector<int> myVec;
        myVec.push_back(0);
        myVec.push_back(1);
        for (int i = 2; i <= N; ++i) {
            myVec.push_back(myVec[i-1] + myVec[i-2]);
        }
        cout << *(myVec.end() -1) << endl;
        return myVec[N];
    }
//        if (N == 0) {
//            return 0;
//        } else if (N==1) {
//            return 1;
//        } else {
//            return fib(N-1) + fib(N-2);
//        }
//    }
};

int main() {
    Solution *s = new Solution();
    cout << s -> fib(5) << endl;
    return 0;
}