# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reversed_node_values_1 = self.build_reversed_ll_str_values(l1)
        reversed_node_values_2 = self.build_reversed_ll_str_values(l2)
        value_1 = int("".join(reversed_node_values_1))
        value_2 = int("".join(reversed_node_values_2))

        total = value_1 + value_2
        total_digits = [int(str_digit) for str_digit in list(str(total))]
        return self.build_ll(total_digits)


    def build_reversed_ll_str_values(self, node: Optional[ListNode]) -> List[int]:
        current_node = node
        node_values: List[int] = [] 

        while current_node:
            node_values.append(str(current_node.val))
            current_node = current_node.next

        node_values.reverse()

        return node_values

    def build_ll(self, values: List[int]) -> ListNode:
        root = ListNode(values.pop())
        current_node = root

        while values:
            current_node.next = ListNode(values.pop())
            current_node = current_node.next

        return root
