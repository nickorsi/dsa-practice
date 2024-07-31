/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function deleteMiddle(head: ListNode | null): ListNode | null {
    // Traverse LL in while loop to determine size of LL
    let count = 1;
    let node = head;
    while(node.next !== null) {
        count ++;
        node = node.next;
    }

    if (count === 1) return null;
    if (count === 2) {
        head.next = null;
        return head;
    }
    // Determine middle value based on size of LL / 2 rounded down
    let middleValue = Math.floor(count / 2);
    // Travverse to middle based on value above and retain previousNode
    let previousNode = null;
    let currentNode = head
    let nextNode = null;


    while(middleValue >= 0) {
        if (middleValue === 0) {
            nextNode = currentNode.next;
            break;
        }
        middleValue --;
        previousNode = currentNode;
        currentNode = currentNode.next;
    }

    previousNode.next = nextNode;

    return head;
};