    def preorder_print(self, root):
        if not root:
            return []
        return [root.val] + self.inorderTraversal(root.left) + self.inorderTraversal(root.right)