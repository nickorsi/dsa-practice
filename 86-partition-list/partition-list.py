# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        current_node = head
        prev_node: Optional[ListNode] = None
        node_before_last_node_less_than_x: Optional[ListNode] = None
        last_node_less_than_x: Optional[ListNode] = None

        while current_node != None:
            # print("current_node= ", current_node)
            # print("prev_node= ", prev_node)
            # print("node_before_last_node_less_than_x= ", node_before_last_node_less_than_x)
            # print("last_node_less_than_x= ", last_node_less_than_x)
            # print("\n")
            if current_node.val >= x:
                if last_node_less_than_x == None:
                    last_node_less_than_x = current_node
                    if prev_node != None:
                        node_before_last_node_less_than_x = prev_node
                prev_node = current_node
                current_node = current_node.next
            else:
                if last_node_less_than_x != None:
                    next_node = current_node.next
                    current_node.next = last_node_less_than_x
                    if node_before_last_node_less_than_x != None:
                        node_before_last_node_less_than_x.next = current_node
                    else:
                        head = current_node
                    node_before_last_node_less_than_x = current_node
                    current_node = next_node
                    prev_node.next = current_node
                else:
                    prev_node = current_node
                    current_node = current_node.next
        
        return head