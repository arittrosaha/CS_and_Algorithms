// You are given two non-empty linked lists representing two non-negative
// integers. The digits are stored in reverse order and each of their nodes
// contain a single digit. Add the two numbers and return it as a linked list.
//
// You may assume the two numbers do not contain any leading zero, except
// the number 0 itself.
//
// Example:
//
// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
// Explanation: 342 + 465 = 807.


/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function addTwoNumbers(head1, head2, carry = 0) {
  if (!head1 && !head2) return null;

  if (!head1) {
    let result = new Node(head2.val);
    result.next = addTwoNumbers(head1, head2.next);
    return result;
  }

  if (!head2) {
    let result = new Node(head1.val);
    result.next = addTwoNumbers(head1.next, head2);
    return result;
  }

  let sum = head1.val + head2.val + carry;
  let ans;

  if (sum > 9) {
    ans = new Node(sum % 10);
    ans.next = addTwoNumbers(head1.next, head2.next, 1);
  } else {
    ans = new Node(sum % 10);
    ans.next = addTwoNumbers(head1.next, head2.next);
  }
}

let l1 = new Node(2);
l1.next = new Node (4);
l1.next.next = new Node (3);

let l2 = new Node(5);
l2.next = new Node(6);
l2.next.next = new Node(4);

console.log(addTwoNumbers(l1, l2));


// function LLNumber(ll) {
//   if (ll.next === null) return ll.val;
//   console.log(ll);
//   let numbers = [];
//   numbers += (ll.val);
//   numbers += (LLNumber(ll.next));
//   return numbers;
// }

// console.log(lln(l1));
