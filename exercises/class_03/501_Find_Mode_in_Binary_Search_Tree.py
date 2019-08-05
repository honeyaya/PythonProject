# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        d = {}

        def dfs(root):
            if not root:
                return

            if root.val not in d:
                d[root.val] = 0

            d[root.val] += 1

            dfs(root.left)

            dfs(root.right)

        dfs(root)
        num = 0

        for key in d:
            if d[key] > num:
                num = d[key]

        res = []
        for key in d:
            if d[key] == num:
                res.append(key)

        return res