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
            if not current_l2:
                current_merged.next=current_l1
                return merged_list_dummy_head.next
            if not current_l1:
                current_merged.next=current_l2
                return merged_list_dummy_head.next
            if current_l1 and current_l2 :
                if current_l1.val < current_l2.val :
                    current_merged.next=current_l1
                    current_l1= current_l1.next
                else:
                    current_merged.next=current_l2
                    current_l2= current_l2.next
                current_merged = current_merged.next
        return merged_list_dummy_head.next