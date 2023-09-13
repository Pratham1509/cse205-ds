# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        lenA,lenB=0,0
        nodeA,nodeB=headA,headB
        while nodeA:
            lenA+=1
            nodeA=nodeA.next
        while nodeB:
            lenB+=1
            nodeB=nodeB.next
        diff=abs(lenA-lenB)
        if lenA>lenB:
            while diff>0:
                headA=headA.next
                diff-=1
        else:
            while diff>0:
                headB=headB.next
                diff-=1
        while headA and headB:
            if headA==headB:
                return headA
            else:
                headA=headA.next
                headB=headB.next
        return None