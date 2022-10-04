# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #Recursive SOLUTION
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        start = None    
        if l1.val < l2.val:
            start = l1;
            start.next = self.mergeTwoLists(l1.next, l2)
        else:
            start = l2;
            start.next = self.mergeTwoLists(l1, l2.next)
        
        return start
    
    #Iterative SOLUTION
    
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        
        dummy = ListNode()
        pointer = dummy
        
        while(list1 and list2):
            if(list1.val < list2.val):
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
            
        if(list1):
            pointer.next = list1
        elif(list2):
            pointer.next = list2
                
        return dummy.next