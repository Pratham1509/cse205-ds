# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        m,n=0,len(nums)-1
        while m<=n:
            if nums[m]!=nums[n]:
                return False
            m+=1
            n-=1
        return True