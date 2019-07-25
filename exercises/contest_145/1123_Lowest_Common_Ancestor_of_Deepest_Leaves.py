# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root

        leaves = []

        def finddepth(root):
            if root == None or (root.left == None and root.right == None):
                return 0
            return max(finddepth(root.left), finddepth(root.right)) + 1

        def findleaves(root, depth):
            if root.left == None and root.right == None:
                if depth == maxdepth:
                    leaves.append(root.val)
                return

            if root.left != None:
                findleaves(root.left, depth + 1)

            if root.right != None:
                findleaves(root.right, depth + 1)

        maxdepth = finddepth(root)

        findleaves(root, 0)
        res = []

        def findAncestor(root):
            if root == None:
                return 0

            if root.left == None and root.right == None:
                if root.val in leaves:
                    if len(leaves) == 1:
                        res.append(root)
                    return 1
                else:
                    return 0
            ans = findAncestor(root.left) + findAncestor(root.right)
            if ans == len(leaves):
                res.append(root)

            return ans

        findAncestor(root)
        return res[0]
