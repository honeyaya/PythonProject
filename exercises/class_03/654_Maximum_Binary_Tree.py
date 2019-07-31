# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def mergeTree(nums, begin, end):
            if begin == end:
                leave = TreeNode(nums[begin])
                return leave

            maxpos = begin
            maxnum = nums[begin]
            for idx in range(begin, end + 1):
                if nums[idx] > maxnum:
                    maxnum = nums[idx]
                    maxpos = idx

            root = TreeNode(maxnum)

            if maxpos != begin:
                root.left = mergeTree(nums, begin, maxpos - 1)

            if maxpos != end:
                root.right = mergeTree(nums, maxpos + 1, end)

            return root

        return mergeTree(nums, 0, len(nums) - 1)