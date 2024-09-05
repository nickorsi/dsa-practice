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

function oddEvenList(head: ListNode | null): ListNode | null {
    // Iterate through LL and count nodes
    let currentNode = head;
    let count = 1;

    while(currentNode !== null && currentNode.next !== null) {
        count ++;
        currentNode = currentNode.next;
    }
    // If LL is smaller than 3 nodes, nothing to change
    if (count < 3) return head;
    // Assign tailNode to currentNode to assist with LL rearrangement
    let tailNode = currentNode;
    // Assign rearrachmentMoves to floor of count / 2
    let rearrangmentMoves = Math.floor(count / 2);
    // Rearragnment depends on LL count
    // If even, must move odds to the tailNode, then when moves all out, take all evens to the back
    let currentOddNode = head;
    let currentEvenNode = currentOddNode.next;

    if (count % 2 === 0) {
        const startEvenNode = head.next;

        while(rearrangmentMoves > 0) {
            // console.log(head, head.next)
            // Move odds to the back
            tailNode.next = currentOddNode;
            // Connect the evennode to the next even node
            // Reassign current Nodes for next round
            // If not on first move, reassign the EvenNode.next
            if (rearrangmentMoves !== Math.floor(count / 2)) {
                currentEvenNode.next = currentOddNode.next;
                currentEvenNode = currentEvenNode.next;
            }
            currentOddNode = currentEvenNode.next;
            // Reassign tailNode
            tailNode = tailNode.next;
            tailNode.next = null;
            // Decrement moves
            rearrangmentMoves --;
        }
        // Now currentOddNode is really the last evenNode and currentEvenNode is really the first oddNode
        // Need to pull evenNodes to back and return the head
        // console.log('after', head, head.next)
        tailNode.next = startEvenNode;
        currentEvenNode.next = null;

        // console.log('end', head, head.next)
        return head;
    // Otherwise if LL is odd, can just move even nodes to the back
    } else {
        while(rearrangmentMoves > 0) {
            // Move evens to back
            tailNode.next = currentEvenNode;
            // Tie in currentOdd to next odd node
            currentOddNode.next = currentEvenNode.next;
            // Reassign current nodes
            currentOddNode = currentOddNode.next;
            currentEvenNode = currentOddNode.next;
            // Reassign tailNode
            tailNode = tailNode.next;
            tailNode.next = null;
            // Decrement moves
            rearrangmentMoves --;
        }
        // Can now just return the head
        return head;
    }   
};