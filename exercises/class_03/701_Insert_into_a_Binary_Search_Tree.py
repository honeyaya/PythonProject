# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        lastNode = TreeNode(val)

        if not root:
            return lastNode

        def dfs(root):
            if val < root.val:
                if root.left:
                    dfs(root.left)
                else:
                    root.left = lastNode
                    return

            if val > root.val:
                if root.right:
                    dfs(root.right)
                else:
                    root.right = lastNode
                    return

        dfs(root)

        return root

'''

[5,null,14,10,77,null,null,null,95,null,null]
4

[5975,2848,9229,1432,2965,8619,9601,756,2691,null,5435,7449,8901,9352,9747,233,952,1650,2699,4410,5616,6956,7627,8631,9185,9322,null,9643,9915,48,359,810,1332,1491,2065,null,null,3316,5008,5468,5918,6197,7334,7518,7802,null,8665,9012,null,9267,null,9619,9685,9753,null,null,107,314,null,null,null,998,1373,null,1593,1867,2315,3106,4170,4653,5299,null,null,5618,null,6089,6776,7057,null,null,null,null,8142,null,null,null,null,null,null,null,null,9677,null,null,9820,null,null,null,null,null,1025,null,null,null,null,1700,1911,null,null,null,3191,3901,4327,null,4869,null,null,null,5656,6013,null,6504,6871,null,7319,8022,8255,null,null,null,null,null,null,null,1818,null,1935,3185,3204,3830,4113,null,null,4788,null,null,5746,null,6070,6331,6546,6841,null,null,null,7939,null,null,8277,null,null,null,null,null,null,null,null,3368,null,3949,4150,null,null,null,null,null,null,null,6503,null,null,null,null,7823,null,null,null,null,3552,null,null,null,null,6349,null,null,null,null,null,null,null]
7363

'''