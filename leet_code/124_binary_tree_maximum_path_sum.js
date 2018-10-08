// Given a non-empty binary tree, find the maximum path sum.
//
// For this problem, a path is defined as any sequence of nodes from some
// starting node to any node in the tree along the parent-child connections.
// The path must contain at least one node and does not need to go through the root.
//
// Example 1:
//
// Input: [1,2,3]
//
//        1
//       / \
//      2   3
//
// Output: 6
// Example 2:
//
// Input: [-10,9,20,null,null,15,7]
//
//    -10
//    / \
//   9  20
//     /  \
//    15   7
//
// Output: 42

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @return {number}
 */


function maxPathSum(root) {
  let max = -Infinity;
  _maxPath(root);
  return max;

  function _maxPath(root) {
    if (!root) return 0;

    let lsum = _maxPath(root.left);
    let rsum = _maxPath(root.right);

    let leftSum = Math.max(0, lsum);
    let rightSum = Math.max(0, rsum);

    let thisMax = root.val + leftSum + rightSum;
    max = Math.max(max, thisMax);

    return root.val + Math.max(leftSum, rightSum);
  }
}


// var maxPathSum = function(root, tempCarry = 0, path = {"sum": 0}) {
//   if (!root) return 0;
//
//   let left = maxPathSum(root.left, tempCarry, path);
//   tempCarry = left + root.val;
//   let right = maxPathSum(root.right, tempCarry, path);
//
//   let leftRoot = left + root.val;
//   let rightRoot = right + tempCarry;
//   let leftRight = left + root.val + right;
//
//   if (leftRight > leftRoot && leftRight > rightRoot) {
//     tempCarry = leftRight;
//   } else if (leftRoot > rightRoot) {
//     tempCarry = leftRoot;
//   } else if (rightRoot > leftRoot){
//     tempCarry = rightRoot;
//   } else {
//     tempCarry = root.val;
//   }
//
//   return carry;
// };
