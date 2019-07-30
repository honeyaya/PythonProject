# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        if not root:
            return []

        queue = []
        res = []

        queue.append(root)
        res.append(root.val)

        while queue:
            onewidth = len(queue)
            onesum = 0
            onenum = 0

            for idx in range(onewidth):
                if queue[idx].left:
                    onenum += 1
                    onesum += queue[idx].left.val
                    queue.append(queue[idx].left)
                if queue[idx].right:
                    onenum += 1
                    onesum += queue[idx].right.val
                    queue.append(queue[idx].right)

            queue = queue[onewidth:]
            if onenum:
                res.append(onesum*1.0/onenum)

        return res

