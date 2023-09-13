# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        nodes=[]
        count=0
        curr=head
        while curr:
            nodes.append(curr)
            count+=1
            curr=curr.next
            if count==k:
                count=0
                m,n=0,k-1
                while m<n:
                    nodes[m].val,nodes[n].val=nodes[n].val,nodes[m].val
                    m,n=m+1,n-1
                nodes=[]
        return head