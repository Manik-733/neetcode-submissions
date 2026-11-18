class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {}

        for i, value in enumerate(inorder):
            inorder_map[value] = i

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)

            mid = inorder_map[root_value]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)