# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node, result):
            if not node:
                return
            dfs(node.left, result)
            result.append(node.val)
            dfs(node.right, result)
        result = []
        dfs(root, result)
        if len(result) < 2:
            return False
        result.sort()
        left = 0
        right = len(result) - 1
        while left < right:
            current_sum = result[left] + result[right]
            if current_sum == k:
                return True
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        return False
99