# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    allsum = 0
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0

        def dfsTilt(root):
            if root == None:
                return 0

            leftTilt = 0
            if root.left != None:
                leftTilt = dfsTilt(root.left)

            rightTile = 0
            if root.right != None:
                rightTile = dfsTilt(root.right)

            thisTile = abs(leftTilt - rightTile)
            self.allsum += thisTile
            return leftTilt + rightTile + root.val

        self.allsum = 0
        dfsTilt(root)
        return self.allsum
