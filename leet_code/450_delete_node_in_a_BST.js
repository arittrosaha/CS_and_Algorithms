// Given a root node reference of a BST and a key, delete the node with the
// given key in the BST. Return the root node reference (possibly updated)
// of the BST.
//
// Basically, the deletion can be divided into two stages:
//
// 1. Search for a node to remove.
// 2. If the node is found, delete the node.
//
// Note: Time complexity should be O(height of tree).
//
// Example:
// root = [5,3,6,2,4,null,7]
// key = 3
//
//     5
//    / \
//   3   6
//  / \   \
// 2   4   7
//
// Given key to delete is 3. So we find the node with value 3 and delete it.
//
// One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
//
//     5
//    / \
//   4   6
//  /     \
// 2       7
//
// Another valid answer is [5,2,6,null,4,null,7].
//
//     5
//    / \
//   2   6
//    \   \
//     4   7
//
// Definition for a binary tree node.
function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

/**
 * @param {TreeNode} root
 * @param {number} key
 * @return {TreeNode}
 */

// leaf
// 1 child
// 2 child

var deleteNode = function(root, key, parent = null) {
    if (!root) return null;

    if (key < root.val) {
        deleteNode(root.left, key, root);
    } else if (key > root.val) {
        deleteNode(root.right, key, root);
    } else {
        if (!root.left && !root.right) {                                        // if it is a leaf
          leafDelete(root, parent);
        } else if ((!root.left && root.right) || (!root.right && root.left)) {  // if it has 1 child
          oneChildDelete(root, parent);
        } else {                                                                // else it has 2 children
            let successor = twoChildDelete(root, parent);
            deleteNode(root.right, successor.val, root);
        }
    }

    if (root.val === null && parent === null) return null;

    return root;
};

function leafDelete(root, parent) {
  if (!parent) {
    root.val = null;
  } else if (root === parent.left){
    parent.left = null;
  } else {
    parent.right = null;
  }
}

function oneChildDelete(root, parent) {
  const left = root.left;
  const right = root.right;
  if (!parent) {
    if (left) {
      root.left = null;
      root.val = left.val;
    } else {
      root.right = null;
      root.val = right.val;
    }
  } else if (parent.left === root) {
    parent.left = left || right;
  } else {
    parent.right = left || right;
  }
}

function twoChildDelete(root) {
    let successor = leftMost(root.right);
    root.val = successor.val;
    return successor;
}

function leftMost(node) {
  if (!node) return null;
  let left = leftMost(node.left);
  return left || node;
}


// let a = new TreeNode(3);
// let b = new TreeNode(4);
// let asLeft = a.left;
// asLeft = b;
// console.log(a.left);

let five = new TreeNode(5);
let three = new TreeNode(3);
let six = new TreeNode(6);
let two = new TreeNode(2);
let four = new TreeNode(4);
let seven = new TreeNode(7);
let one = new TreeNode(1);
let zero = new TreeNode(0);

// five.left = three;
// five.right = six;
// three.left = two;
// three.right = four;
// six.right = seven;

// two.left = one;
// two.right = three;

console.log(deleteNode(zero, 0));
