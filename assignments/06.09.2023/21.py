# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        else:
            tmp=ListNode()
            if list1.val>list2.val:
                tmp=list2
                tmp.next=self.mergeTwoLists(list1,list2.next)
            else:
                tmp=list1
                tmp.next=self.mergeTwoLists(list1.next,list2)
            return tmp