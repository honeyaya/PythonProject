# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root == None:
            return ans

        # preorder root->left->right
        def dfs(root):
            if root == None:
                return

            ans.append(root.val)

            if root.left != None:
                dfs(root.left)

            if root.right != None:
                dfs(root.right)

        dfs(root)

        return ans