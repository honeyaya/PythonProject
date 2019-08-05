# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root.val == x or root.val == y:
            return False

        def findDepth(root, value, depth):
            if root.val == value:
                return depth

            ldepth = None
            rdepth = None

            if root.left:
                ldepth = findDepth(root.left, value, depth + 1)
            if root.right:
                rdepth = findDepth(root.right, value, depth + 1)

            if ldepth:
                return ldepth
            return rdepth

        xdepth = findDepth(root, x, 0)
        print(xdepth)

        ydepth = findDepth(root, y, 0)
        print(ydepth)

        if xdepth != ydepth:
            return False

        def sameParent(root, depth):
            if not root:
                return False

            if depth == xdepth - 1:
                if root.left and root.right:
                    if root.left.val == x and root.right.val == y:
                        return True
                    if root.left.val == y and root.right.val == x:
                        return True
                    return False
                return False
            
            if depth > xdepth - 1:
                return False

            return sameParent(root.left, depth + 1) or sameParent(root.right, depth + 1)

        if sameParent(root, 0):
            return False

        return True
