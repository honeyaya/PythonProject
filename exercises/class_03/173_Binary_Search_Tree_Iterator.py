# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nums = []
        self.inorder(root)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.nums.append(root.val)
        self.inorder(root.right)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        tmp = self.nums[0]
        self.nums = self.nums[1:]
        return tmp

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.nums) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
