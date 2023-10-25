# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root, x, y):
        ans = []
        ans.append((x, y, root.val))
        if root.left:
            ans += self.traversal(root.left, x - 1, y + 1)
        if root.right:
            ans += self.traversal(root.right, x + 1, y + 1)
        return ans

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = self.traversal(root, 0, 0)
        ans.sort(key=lambda item: (item[0], item[1], item[2]))
        result = []
        current_x = None
        current_group = []
        for x, y, val in ans:
            if x != current_x:
                if current_group:
                    result.append(current_group)
                current_x = x
                current_group = [val]
            else:
                current_group.append(val)
        if current_group:
            result.append(current_group)
        return result