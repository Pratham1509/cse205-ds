# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr =  head
        while curr:
            j = head
            while j != curr:
                if j.val > curr.val:
                    j.val, curr.val = curr.val, j.val
                j = j.next
            curr = curr.next
        return head
        