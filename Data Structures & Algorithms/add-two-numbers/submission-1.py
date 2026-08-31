# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def add_numbers(self, l1: ListNode, l2: ListNode | None, carry: int = 0) -> int:
        sum: int = l1.val + (l2.val if l2 else 0) + carry
        carry = sum // 10
        l1.val = sum % 10

        if l1.next or (l2 and l2.next):
            if not l1.next:
                l1.next = ListNode()

            return self.add_numbers(l1.next, l2.next if l2 else None, carry)

        return carry


    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry = self.add_numbers(l1, l2)
        if carry > 0:
            last = l1
            while last.next:
                last = last.next
            last.next = ListNode(carry)
        return l1