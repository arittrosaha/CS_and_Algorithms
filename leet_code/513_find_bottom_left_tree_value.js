// Given a binary tree, find the leftmost value in the last row of the tree.

// Example 1:
// Input:

//      2
//     / \
//    1   3

// Output: 1

// Example 2:
// Input:

//      1
//     / \
//    2   3
//   /   /  \
// 4     5   6
//      /
//     7

// Output: 7
// Note: You may assume the tree (i.e., the given root node) is not NULL.

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

// function getHeight(root) {
//     if (!root) return -1;

//     return Math.max(getHeight(root.left), getHeight(root.right)) + 1;
// }

// Alvin's solution
function findBottomLeftValue1(root) {
    let memo = {};
    traverse(root, memo);
    let depths = Object.keys(memo).map(Number).sort((a, b) => a - b);
    let maxDepth = depths[depths.length - 1];
    return memo[maxDepth];
}

function traverse(root, memo, depth = 0) {
    if (!root) return;
    if (!(String(depth) in memo)) memo[depth] = root.val;
    traverse(root.left, memo, depth + 1);
    traverse(root.right, memo, depth + 1);
}

// Chao's solution
var findBottomLeftValue2 = function (root, parent = null) {
    if (!root) return [Infinity, -1];
    let left = findBottomLeftValue2(root.left, root);
    let right = findBottomLeftValue2(root.right, root);
    let maxArr = left[1] >= right[1] ? left : right;
    maxArr[1]++;
    if (maxArr[0] === Infinity) maxArr[0] = root.val;
    return parent ? maxArr : maxArr[0];
};