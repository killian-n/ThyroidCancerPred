# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], current_node: Optional[ListNode]=None, carry=0) -> Optional[ListNode]:
        next_node = None
        l1_next = None
        l2_next = None
        l1_val = 0
        l2_val = 0
        carry = 0
        l3 = current_node
        if l1:
            l1_val = l1.val
            if l1.next:
                l1_next = l1.next
        if l2:
            l2_val = l2.val
            if l2.next:
                l2_next = l2.next
        sum_val = l1_val + l2_val + carry
        if sum_val > 9:
            carry = 1
            sum_val = sum_val % 10
        if not l3:
            l3 = ListNode()
        l3.val = sum_val
        if l1_next or l2_next:
            l3.next = ListNode()
            return self.addTwoNumbers(l1_next, l2_next, current_node=l3.next,carry=carry)
        return l3
    
if __name__ == '__main__':
  node = ListNode(val=3)
  node2 = ListNode(val=4)
  node3 = ListNode(val=3)
  node.next = node2
  node2.next = node3

  node4 = ListNode(5)
  node5 = ListNode(6)
  node6 = ListNode(4)
  node4.next = node5
  node5.next = node6
  sol = Solution()
  ans = sol.addTwoNumbers(node, node4)
  while ans:
    print(ans.val)
    ans = ans.next