// Given a binary tree, flatten it to a linked list in-place.
//
// For example, given the following tree:
//
//     1
//    / \
//   2   5
//  / \   \
// 3   4   6
// The flattened tree should look like:
//
// 1
//  \
//   2
//    \
//     3
//      \
//       4
//        \
//         5
//          \
//           6
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */

var flatten = function(root) {
  if (root) {
    flattenActual(root)
  }
}

var flattenActual = function(root) {
  if (!root.left && !root.right) return root;

  let rightRoot = root.right;
  if (root.left) {
    var leftTail = flattenActual(root.left);
    root.right = root.left;
    leftTail.right = rightRoot;
    root.left = null;
  }

  if (rightRoot) {
    return flattenActual(rightRoot);
  } else {
    return leftTail;
  }
};
