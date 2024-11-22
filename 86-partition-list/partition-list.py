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
            # Is the current_node value greater than or equal to x
            if current_node.val >= x:
                # Is last_node_less_than_x EQUAL to None
                if last_node_less_than_x == None:
                    # Assign it to the current_node
                    last_node_less_than_x = current_node
                    # If prev_node NOT equal to None
                    if prev_node != None:
                        # Assign node_before_last_node to prev_node
                        node_before_last_node_less_than_x = prev_node
                # Assign prev_node to current_node
                prev_node = current_node
                # Assign current_node to current_node.next
                current_node = current_node.next
            # Else
            else:
                # Is last_node_less_than_x NOT equal to None      
                if last_node_less_than_x != None:
                    # Save next node
                    next_node = current_node.next
                    # Assign next value of current_node to last_node_less_than_x
                    current_node.next = last_node_less_than_x
                    # If node_before_last_node_less_than_x NOT equal to None
                    if node_before_last_node_less_than_x != None:
                        # Assign node_before_last_node_less_than_x to current_node
                        node_before_last_node_less_than_x.next = current_node
                    else:
                        head = current_node
                    # Reassign both node_before_last_node_less_than_x
                    node_before_last_node_less_than_x = current_node
                    # # Assign current_node to current_node.next
                    current_node = next_node
                    prev_node.next = current_node
                else:
                    # Assign prev_node to current_node
                    prev_node = current_node
                    # Assign current_node to current_node.next
                    current_node = current_node.next
        
        # Return head
        return head