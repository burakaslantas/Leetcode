# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        dummy = ListNode(0)
        current = dummy
        #edge cases:
        #if l1 and l2 empty
        #return an empty list
        
        #if one of the list of l1 or l2 is empty:
        #return l1 or l2 which is non empty list
        
        while l1 and l2:
            if l1.val >= l2.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            current = current.next
        current.next = l1 or l2
        return dummy.next
        #start first element of l2 and pass one by one
        #compare element l1 and l2
            #if l1 element >= l2 element:
                #add l2 element into result list
            #else l1 element < l2 element:
                #add l1 element into result list
        #return result list