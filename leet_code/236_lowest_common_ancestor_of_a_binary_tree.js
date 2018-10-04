// Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
//
// According to the definition of LCA on Wikipedia: “The lowest common ancestor
// is defined between two nodes p and q as the lowest node in T that has both
// p and q as descendants (where we allow a node to be a descendant of itself).”
//
// Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
//
//         _______3______
//        /              \
//     ___5__          ___1__
//    /      \        /      \
//    6      _2       0       8
//          /  \
//          7   4
// Example 1:
//
// Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
// Output: 3
// Explanation: The LCA of of nodes 5 and 1 is 3.
// Example 2:
//
// Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
// Output: 5
// Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
//              according to the LCA definition.
// Note:
// - All of the nodes' values will be unique.
// - p and q are different and both values will exist in the binary tree.

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */

var lowestCommonAncestor = function(root, p, q) {
  let que = [root];
  let lowestCommonAncestor;

  while (que.length) {
    const node = que.shift();
    if (node.left) que.push(node.left);
    if (node.right) que.push(node.right);

    if (checkDescendentsDFS(que[i], p, memo) && checkDescendentsDFS(que[i], q, memo)) {
      lowestCommonAncestor = node;
      break;
    }
  }

  return lowestCommonAncestor;
};

var checkDescendentsDFS = function(root, targetNode, memo) {
  if (!root) return null;
  if (!targetNode) return null;
  if (root.val === targetNode.val) return true;

  let key = `${root.val}-${targetNode.val}`
  if (key in memo) return memo[key];

  if (checkDescendentsDFS(root.left, targetNode, memo)){
    memo[key] = true;
    return memo[key];
  }
  if (checkDescendentsDFS(root.right, targetNode, memo)) {
    memo[key] = true
    return memo[key];
  }
  memo[key] = false;
  return memo[key];
}

var lowestCommonAncestorMemo = function(root, p, q, memo={}) {
  let que = [root];
  let lowestCommonAncestor;

  let i = 0;
  while (i < que.length) {
    const node = que[i];
    if (node.left) que.push(node.left);
    if (node.right) que.push(node.right);

    i += 1;
  }

  for (let i = que.length-1; i >= 0; i--) {
    if (checkDescendentsDFS(que[i], p, memo) && checkDescendentsDFS(que[i], q, memo)) {
      return que[i];
    }
  }
};

var checkDescendentsMemo = function(root, targetNode, memo) {
  if (!root) return null;
  if (!targetNode) return null;
  if (root.val === targetNode.val) return true;

  let key = `${root.val}-${targetNode.val}`
  if (key in memo) return memo[key];

  if (checkDescendentsDFS(root.left, targetNode, memo)){
    memo[key] = true;
    return memo[key];
  }
  if (checkDescendentsDFS(root.right, targetNode, memo)) {
    memo[key] = true
    return memo[key];
  }
  memo[key] = false;
  return memo[key];
}

function lowestCommonAncestorLLSOL(root, p, q) {
  if (!root || root === p || root === q) return root;
  var resL = lowestCommonAncestorLLSOL(root.left, p, q);
  var resR = lowestCommonAncestorLLSOL(root.right, p, q);
  return (resL && resR) ? root : (resL || resR);
}

// Definition for a binary tree node.
function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

var three = new TreeNode(3);
var five = new TreeNode(5);
var one = new TreeNode(1);
var six = new TreeNode(6);
var two = new TreeNode(2);
var seven = new TreeNode(7);
var four = new TreeNode(4);
var zero = new TreeNode(0);
var eight = new TreeNode(8);
three.left = five;
three.right = one;
five.left = six;
five.right = two;
two.left = seven;
two.right = four;
one.left = zero;
one.right = eight;
