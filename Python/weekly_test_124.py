# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # get node length
    def node_length(self, root, x):
        if root is None:
            return -9999999
        if root.val == x:
            return 0
        else:
            return max(self.node_length(root.left, x)+1, self.node_length(root.right, x)+1)

    # get parent node val
    def node_parent(self, root, x):
        if (root.val == x) or (root is None):
            return -9999999
        else:
            if not(root.left is None):
                if root.left.val == x:
                    return root.val
            elif not(root.right is None):
                if root.right.val == x:
                    return root.val
            else:
                return max(self.node_parent(root.left, x), self.node_parent(root.right, x))

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if self.node_length(root, x) != self.node_length(root,y):
            return False
        else:
            if self.node_parent(root, x) == self.node_parent(root, y):
                return True
            else:
                return False

if __name__ == '__main__':
    m = None
    s = Solution()