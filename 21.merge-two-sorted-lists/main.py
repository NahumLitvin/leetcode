from typing import *
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list_dummy_head = ListNode()
        current_l1 = list1
        current_l2 = list2
        current_merged = merged_list_dummy_head
        
        while (current_l1 or current_l2):
            val1 = current_l1.val if current_l1 else 101
            val2 = current_l2.val if current_l2 else 101
            if val1 < val2 :
                current_merged.next=ListNode(val1)
                current_l1= current_l1.next
            else:
                current_merged.next=ListNode(val2)
                current_l2= current_l2.next
            current_merged = current_merged.next
        return merged_list_dummy_head.next