# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#   Can have empty LL, so do first check and return if this is the case
        if not head: return head
#   Have two pointers one at head other at head.next
        pointer1 = head
        pointer2 = head.next
#   While pointers are truthy
        while pointer2:
#       If pointers are the same
            if pointer1.val == pointer2.val:
#           Assign pointer1.next to pointer2.next
                pointer1.next = pointer2.next
#           Only advance pointer2 to pointer2.next
                pointer2 = pointer2.next
#       Else
            else:
#           Advance boths pointers to next value
                pointer1 = pointer1.next
                pointer2 = pointer2.next
#   Return head? 
        return head