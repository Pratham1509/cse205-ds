# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        x=[]
        if root is None:
            return x
        queue=deque([])
        queue.append(root)
        while len(queue)!=0:
            queue_level=len(queue)
            for i in range(queue_level):
                current=queue.popleft()
                if i==(queue_level-1):
                    x.append(current.val)
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
        return x
        