# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Iterative Approach
        Solution #1
        previous = None
        while(head != None):
            current = head
            head = head.next
            current.next = previous
            previous = current
        return previous
        """
        
    #Recursive Approach
    #Solution #2
        return self.helper(head)
    
    def helper(self, node, previous = None):
        if(node == None):
            return previous
        else:
            n = node.next
            node.next = previous
            return self.helper(n, node)