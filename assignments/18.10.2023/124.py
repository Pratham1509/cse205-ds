# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pathSum=float('-inf')      
        def dfs(node):
            nonlocal pathSum            
            if not node:
                return 0
            leftSum= max(dfs(node.left),0)
            rightSum=max(dfs(node.right),0)            
            current=node.val+leftSum+rightSum            
            pathSum=max(pathSum,current)       
            return node.val+max(leftSum,rightSum)
        dfs(root)
        return pathSum
        