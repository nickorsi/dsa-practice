from collections import deque 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
# #   Find middle of LL
#         half_ll_length = 0
#         previous_orig = None
#         slow = head
#         fast = head.next.next

#         while fast and fast.next:
#             half_ll_length += 1
#             previous_orig = slow
#             slow = slow.next
#             fast = fast.next.next

# #   Reverse second half of LL
#         current = slow.next
#         previous_new = None

#         while current:
#             next_node = current.next
#             current.next = previous_new
#             previous_new = current
#             current = next_node
    
# # Reassign middle of LL to the reversed portion of the LL
#         slow.next = previous_new
# #   Iterate through LL with two pointers, one at head and other at n+1/2
#         pointer2 = head
#         for position in range(half_ll_length):
#             pointer2 = pointer2.next

#         pointer1 = head
#         pointer2 = pointer2.next
#         max_sum = float('-inf')

#         while pointer2:
#             max_sum = max(max_sum, pointer1.val + pointer2.val)
#             pointer1 = pointer1.next
#             pointer2 = pointer2.next

#         return max_sum

# Another optional solution
# Iterate through entire LL and add vale to both a stack and queue while also getting count of the LL
        queue = deque()
        stack = []
        count = 0
        current_node = head

        while current_node != None:
            count += 1
            stack.append(current_node.val)
            queue.append(current_node.val)
            current_node = current_node.next
        # print(count, int(count/2))
# Then iterate through half the count, summing the stack and queue values and keeping track of the max
        max_count = float('-inf')
        for _ in range(int(count/2)):
            max_count = max(max_count, stack.pop() + queue.popleft())

# Return the max
        return max_count