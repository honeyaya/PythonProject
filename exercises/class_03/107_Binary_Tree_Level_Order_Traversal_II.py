# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        queue = []

        res = []

        queue.append(root)
        res.append([root.val])

        while queue:
            tmp = []
            onewidth = len(queue)
            for idx in range(onewidth):
                if queue[idx].left :
                    queue.append(queue[idx].left)
                    tmp.append(queue[idx].left.val)
                if queue[idx].right:
                    queue.append(queue[idx].right)
                    tmp.append(queue[idx].right.val)
            queue = queue[onewidth:]
            if tmp:
                res.append(tmp)

        return res[::-1]