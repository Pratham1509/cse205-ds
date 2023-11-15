# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def fun(self, data):
        new_node = TreeNode(data)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current:
            if new_node.val < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    break
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        res = Solution()
        res.head = None
        for i in preorder:
            res.fun(i)
        return res.head
        