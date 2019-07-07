class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """

        ans = []
        if root == None:
            return ans
        ans.append(root)

        def find(tree, value):
            if tree == None:
                return None

            if tree.left != None and tree.left.val == value:
                if tree.left.left != None:
                    ans.append(tree.left.left)
                if tree.left.right != None:
                    ans.append(tree.left.right)
                tree.left = None
                return tree

            if tree.right != None and tree.right.val == value:
                if tree.right.left != None:
                    ans.append(tree.right.left)
                if tree.right.right != None:
                    ans.append(tree.right.right)
                tree.right = None
                return tree

            if tree.left != None:
                find(tree.left, value)

            if tree.right != None:
                find(tree.right, value)

        def remove_value(value):
            for tree in ans:
                # print(tree)
                if tree != None and tree.val == value:
                    tmp = tree
                    if tmp != None:
                        if tmp.left != None:
                            ans.append(tmp.left)
                        if tmp.right != None:
                            ans.append(tmp.right)
                        roots.append(tmp)
                else:
                    tmp = find(tree, value)

        roots = []

        for value in to_delete:
            remove_value(value)
            # print("ans:{}".format(ans))

        ss = set()
        for root in roots:
            ans.remove(root)

        for tmp in ans:
            ss.add(tmp)
        return list(ss)