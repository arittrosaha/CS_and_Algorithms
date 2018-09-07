class Node {
  constructor(val) {
    this.val = val;
    this.left = this.right = null;
  }
}

function height(root) { // Time: O(n)
  if (!root) return -1;
  return 1 + Math.max(height(root.left), height(root.right));
}

function isBalanced(root){ // Time: O(n^2)
  if (!root) return true; // a single node is balanced
  let areGoodHeights = Math.abs(height(root.left) - height(root.right)) <= 1;
  return areGoodHeights && isBalanced(root.left) && isBalanced(root.right);
}

// function enumerate(root, id = {id: 0}) {
//   root.id = id.id++;
//   enumerate(root.left);
//   enumerate(root.right);
// }

let a = new Node('a');
let b = new Node('b');
let c = new Node('c');
let d = new Node('d');
let e = new Node('e');
let f = new Node('f');
let g = new Node('g');

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;
f.right = g;

console.log(height(a));
