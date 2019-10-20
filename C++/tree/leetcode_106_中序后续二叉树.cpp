#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};


class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        // 终止条件 如果为0，返回None; 如果为1，返回treeNode
        if (inorder.empty())
            return nullptr;
        if (inorder.size() == 1)
            return new TreeNode(inorder[0]);
        // get root value: postorder[-1]
        auto root = new TreeNode(postorder.back());

        // 查根节点索引
        int index = 0;
        for (int i = 0; i < inorder.size(); ++i) {
            if(inorder[i] == root -> val) {
                index = i;
            }
        }
        // 获得左子树右子树中序遍历和长度
        // C++ 初始化vector
        vector<int> left_in(inorder.begin(), inorder.begin()+index);
        vector<int> right_in(inorder.begin()+index+1, inorder.end());

        // 获得左子树右子树后续遍历和长度，C++从一个vector初始化另一个vector
        vector<int> left_post(postorder.begin(), postorder.begin()+left_in.size());
        vector<int> right_post(postorder.begin()+left_in.size(), postorder.end()-1);

        // 创建根节点，递归创建左右子树
        // C++ 调用自身函数
        root->left = buildTree(left_in, left_post);
        root->right = buildTree(right_in, right_post);
        return root;
    }
};


int main() {


}

