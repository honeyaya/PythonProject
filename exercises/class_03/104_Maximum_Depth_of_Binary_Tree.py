# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        def dfs(root):
            if root == None:
                return 0

            return max(dfs(root.left), dfs(root.right)) + 1

        return dfs(root)
