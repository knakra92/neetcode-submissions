# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_count = 0

        list: ListNode = head

        while list:
            node_count += 1
            list = list.next

        index_to_remove = node_count - n

        if index_to_remove == 0:
            return head.next

        idx = 0
        list = head
        while idx <= index_to_remove:
            if idx == index_to_remove - 1:
                list.next = list.next.next
                idx += 1
            else:
                list = list.next
                idx += 1

        return head