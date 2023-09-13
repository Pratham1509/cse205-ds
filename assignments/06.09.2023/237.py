class Solution:
    def deleteNode(self, node):
        node.val=node.next.val
        if node.next.next:
            node.next=node.next.next
        else:
            node.next=None