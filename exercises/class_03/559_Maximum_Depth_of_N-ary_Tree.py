"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0

        def dfs(root):
            if root == None:
                return 0

            res = 0
            for chid in root.children:
                tmp = dfs(chid)
                res = max(res, tmp)


            return res + 1

        return dfs(root)