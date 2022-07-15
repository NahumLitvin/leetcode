# Definition for singly-linked list.
from math import remainder
from pkgutil import extend_path
from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst = ListNode()
        first = lst
        remainder = 0
        while True:
            sum = 0
            if not l1 and not l2:
                return first.next
            if l1: 
                sum += l1.val
                l1 = l1.next
            if l2: 
                sum += l2.val
                l2 = l2.next
            sum+=remainder         
            lst.next = ListNode(sum % 10)
            remainder = sum // 10            
            lst = lst.next
            
        
lst =  ListNode(2,ListNode(4,ListNode(3)))
lst2 = ListNode(5,ListNode(6,ListNode(4)))

sol =  Solution()
res = sol.addTwoNumbers(lst,lst2)    
while True:
    print(res.val)
    res = res.next
    if not res:
        break