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
    // if (head === null) return head;
    // // Iterate through to get the tail and count
    // let currentNode = head;
    // let count = 1;
    // while(currentNode.next !== null) {
    //     count ++;
    //     currentNode = currentNode.next;
    // }

    // if (count < 2) return head;

    // let tailNode = currentNode;
    // let nextNode = head.next;
    // currentNode = head;

    // // Iterate through again assigning the currentNode to the tail until count is zero
    // while(count !== 1) {
    //     console.log(currentNode, nextNode, tailNode);
    //     currentNode.next = null;
    //     tailNode.next = currentNode;
    //     currentNode = nextNode;
    //     nextNode = currentNode.next;
    //     console.log(currentNode, nextNode, tailNode);
    //     tailNode = tailNode.next;
    //     // console.log(currentNode, tailNode)
    //     count --;
    // }
    // // Return the LL
    // return currentNode;
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