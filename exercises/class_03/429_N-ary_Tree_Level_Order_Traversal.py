"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
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
                if queue[idx].children:
                    for chid in queue[idx].children:
                        if chid:
                            queue.append(chid)
                            tmp.append(chid.val)

            if tmp:
                res.append(tmp)

            queue = queue[onewidth:]

        return res
