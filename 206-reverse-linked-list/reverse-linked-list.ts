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

function reverseList(head: ListNode | null): ListNode | null {
    let prevNode = null;
    let currentNode = head;

    while(currentNode !== null) {
        const nextnode = currentNode.next;

        currentNode.next = prevNode;
        prevNode = currentNode;
        currentNode = nextnode;
    }

    return prevNode;
};