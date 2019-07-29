# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0

        leveldict = {}
        def depth(root):
            if root == None:
                return 0

            return max(depth(root.left), depth(root.right)) + 1

        maxdepth = depth(root)
        print(maxdepth)

        def dfs(root, pos, level):
            if root == None or level == maxdepth:
                return
            if level not in leveldict:
                leveldict[level] = []
                leveldict[level].append(pos)
                leveldict[level].append(pos)

            leveldict[level][0] = min(leveldict[level][0], pos)
            leveldict[level][1] = max(leveldict[level][1], pos)

            if root.left != None:
                dfs(root.left, 2 * pos - 1, level + 1)

            if root.right != None:
                dfs(root.right, 2 * pos, level + 1)

        dfs(root, 1, 0)

        res = 0
        for key in leveldict:
            #print(leveldict[key])
            res = max(res, leveldict[key][1] - leveldict[key][0] + 1)

        return res

