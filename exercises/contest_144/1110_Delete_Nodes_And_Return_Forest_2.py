class Solution(object):
    ans = []
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete_set = ()
        for value in to_delete:
            to_delete_set.add(value)

        self.ans = []

        def dfs(root, is_root):
            if root == None:
                return

            if to_delete_set.find(root.val) != to_delete_set.end():
                dfs(root.left, 1)
                dfs(root.right, 1)
                root = None
            else:
                if is_root == 1:
                    self.ans.append(root)

                dfs(root.left, 0)
                dfs(root.right, 0)

        dfs(root, 1)
        return self.ans