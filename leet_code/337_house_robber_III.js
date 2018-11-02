// The thief has found himself a new place for his thievery again. There
// is only one entrance to this area, called the "root." Besides the root,
// each house has one and only one parent house. After a tour, the smart
// thief realized that "all houses in this place forms a binary tree".
// It will automatically contact the police if two directly-linked houses
// were broken into on the same night.
//
// Determine the maximum amount of money the thief can rob tonight without
// alerting the police.
//
// Example 1:
// Input: [3,2,3,null,3,null,1]
//
//      3
//     / \
//    2   3
//     \   \
//      3   1
//
// Output: 7
// Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
//
// Example 2:
// Input: [3,4,5,1,3,null,1]
//
//      3
//     / \
//    4   5
//   / \   \
//  1   3   1
//
// Output: 9
// Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

// Definition for a binary tree node.
function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}
/**
 * @param {TreeNode} root
 * @return {number}
 */
var rob = function(root) {
  if (!root) return 0;
  if (root.maxLoot !== undefined) return root.maxLoot;

  let next = next_levels(root, 1);
  let next_next = next_levels(root, 2);

  root.maxLoot = Math.max(
    (next.reduce((sum, node) => sum + rob(node), 0)),
    (root.val + next_next.reduce((sum, node) => sum + rob(node), 0))
  )

  return root.maxLoot;
};

function next_levels(root, level) {
  if (!root) return [];
  if (level === 0) return [root];

  return [...next_levels(root.left, level - 1), ...next_levels(root.right, level - 1)];
}

// Testing

// let a = new TreeNode(3);
// let b = new TreeNode(2);
// // let c = new TreeNode(3);
// // let d = new TreeNode(3);
// let e = new TreeNode(1);
// // let f = new TreeNode()
//
// // a.left = b;
// // a.right = c;
// // b.right = d;
// // c.right = e;
//
// // e.left = b;
// // e.right = a;
// console.log(rob(e));
