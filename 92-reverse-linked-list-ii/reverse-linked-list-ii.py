# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
#   If left = right return head
        if left == right: return head
#   Define current node as head
        current = head
#   Define counter as 1
        counter = 1
#   Define prev, start, and end as none
        prev = start = end = None
#   while current is truthy
        while current:
#       if counter = left
            if counter == left:
#           start = prev
                start = prev
#           end = current
                end = current
#           while counter <= right
                while counter <= right:
#               next_node = current.next
                    next_node = current.next
#               current.next = prev
                    current.next = prev
#               if counter = right
                    if counter == right: 
#                   if start truthy then start.next = current
                        if start: start.next = current
#                   end.next = next
                        end.next = next_node
#                   if left = 1 return current
                        if left == 1: return current
#                   else return head
                        else: return head
#               prev = current
                    prev = current
#               current = next_node
                    current = next_node
#               increment counter
                    counter += 1
#       prev = current
            prev = current
#       current = current.next
            current = current.next
#       increment counter
            counter += 1
#   return head
        return head
