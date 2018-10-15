// You are given a binary tree in which each node contains an integer value.
//
// Find the number of paths that sum to a given value.
//
// The path does not need to start or end at the root or a leaf, but it must
// go downwards (traveling only from parent nodes to child nodes).
//
// The tree has no more than 1,000 nodes and the values are in the range
// -1,000,000 to 1,000,000.
//
// Example:
//
// root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
//
//       10
//      /  \
//     5   -3
//    / \    \
//   3   2   11
//  / \   \
// 3  -2   1
//
// Return 3. The paths that sum to 8 are:
//
// 1.  5 -> 3
// 2.  5 -> 2 -> 1
// 3. -3 -> 11

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {number}
 */
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

// function pathSum(root, sum) {
//   if (!root) return 0;
//   let pathNode = paths(root)
//   if (pathNode !== null) {
//      var pathNodeVal = pathNode.map(path=>path.map(node => node.val));
//   }
//   if (pathNodeVal !== undefined) {
//     return pathNodeVal.filter(path => path.reduce((sum, val) => sum + val) === sum).length;
//   }
// }

function Paths(root) {
  if (!root) return null;
  if ((!root.left && !root.right)) return [[root]];

  let allPaths = [];
  let lPaths = paths(root.left);
  let rPaths = paths(root.right);

  if (lPaths !== null) {
    lPaths.forEach(path => allPaths.push(path));
  }

  if (rPaths !== null) {
    rPaths.forEach(path => allPaths.push(path));
  }

  if (lPaths !== null) {
    var lIncluded = lPaths.filter(path => path[0] === root.left || path.length === 0).map(path => [ root, ...path]);
    lIncluded.forEach(path => allPaths.push(path));
  }

  if (rPaths !== null) {
    var rIncluded = rPaths.filter(path => path[0] === root.right || path.length === 0).map(path => [ root, ...path]);
    rIncluded.forEach(path => allPaths.push(path));
  }

  return [ ...allPaths, [ root ] ];
};

function pathSum(root, sum) {
  if (!root) return 0;

  let count = 0;
  let stack = [root];
  while (stack.length) {
    let node = stack.shift();
    if (node.left) stack.push(node.left);
    if (node.right) stack.push(node.right);
    pathsFromRoot(node, 0);
  }

  function pathsFromRoot(root, thisSum) {
    if (!root) return;
    if (thisSum + root.val === sum) {
      count += 1;
    }
    pathsFromRoot(root.left, thisSum + root.val);
    pathsFromRoot(root.right, thisSum + root.val);
  }

  return count;
}


let ten = new TreeNode(10);
let five = new TreeNode(5);
let negthree = new TreeNode(-3);
let ten = new TreeNode(10);
let ten = new TreeNode(10);

two.right = one;

one.left = two;
one.right = three;
two.left = four;
two.right = five;

let p = paths(two).map(path=>path.map(node => node.val));
console.log(p);

// let sums = p.map(path => path.reduce((sum, val) => sum + val)).filter((sum) => sum === 7);
// console.log(sums);
