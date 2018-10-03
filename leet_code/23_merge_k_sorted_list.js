// Merge k sorted linked lists and return it as one sorted list. Analyze and
// describe its complexity.
//
// Example:
//
// Input:
// [
//   1->4->5,
//   1->3->4,
//   2->6
// ]
// Output: 1->1->2->3->4->4->5->6
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */

// time: O(KL)
// K - the number of linked list or length of the given array.
// L - the highest length between h1.length and h2.length.
var mergeKLists1 = function(lists) { // time: O(K)
  if (!lists.length) return null;
  if (lists.length === 1) return lists[0];
  lists[0] = merge(lists[0], lists.pop());
  return mergeKLists(lists);
};

function merge(h1, h2) { // time: O(L);
  if (!h1) return h2;
  if (!h2) return h1;

  if (h1.val < h2.val) {
    h1.next = merge(h1.next, h2);
    return h1;
  } else {
    h2.next = merge(h1, h2.next);
    return h2;
  }
}

// time: O(L*log(K))
const mergeKLists2 = (lists, lo = 0, hi = lists.length - 1) => { // time: O(log(K))
  if (lists.length === 0) {
    return lists;
  }

  if (lo === hi) {
    return lists[lo];
  }

  const mid = Math.floor((hi + lo) / 2);
  const left = mergeKLists(lists, lo, mid);
  const right = mergeKLists(lists, mid + 1, hi);

  return mergeTwoLists(left, right);
};

const mergeTwoLists = (l1, l2) => { // time: O(n)
  if (l1 === null) {
    return l2;
   }
  if (l2 === null) {
    return l1;
   }
  if (l1.val < l2.val) {
    l1.next = mergeTwoLists(l1.next, l2);
    return l1;
  } else {
    l2.next = mergeTwoLists(l1, l2.next);
    return l2;
  }
};
