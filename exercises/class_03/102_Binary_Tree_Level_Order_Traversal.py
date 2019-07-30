# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
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
            onewidth = len(queue)

            tmp = []

            for idx in range(onewidth):
                if queue[idx].left != None:
                    queue.append(queue[idx].left)
                    tmp.append(queue[idx].left.val)
                if queue[idx].right != None:
                    queue.append(queue[idx].right)
                    tmp.append(queue[idx].right.val)

            queue = queue[onewidth:]

            if tmp:
                res.append(tmp)

        return res
    
