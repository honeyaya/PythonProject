# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not  root:
            return True

        def preOrder(root, value):
            if not root:
                return True

            if root.val != value:
                return False

            return preOrder(root.left, value) and preOrder(root.right, value)

        return preOrder(root, root.val)

