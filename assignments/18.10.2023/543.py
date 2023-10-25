# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.getDiameter(root)
        return self.max_diameter
    
    def getDiameter(self, root):
        if not root:
            return 0
        left_depth = self.getDiameter(root.left)
        right_depth = self.getDiameter(root.right)
        diameter = left_depth + right_depth
        self.max_diameter = max(self.max_diameter, diameter)
        return max(left_depth, right_depth) + 1
