class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count=0
        while curr:
            count+=1
            curr=curr.next
        res=head
        for i in range(count//2):
            res=res.next
        return res