class Node {
  constructor(val) {
    this.val = val;
    this.left = this.right = null;
  }
}

function isBalanced(root) {
  if (!root) return true;
  let areDepthsGood = Math.abs(getDepth(root.left) - getDepth(root.right)) < 2;
  return areDepthsGood && isBalanced(root.left) && isBalanced(root.right);
}

function getDepth(root) {
  if (!root) return -1;
  return 1 + Math.max(getDepth(root.left), getDepth(root.right));
}

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
c.left = f;
c.right = g;

let w = new Node('w');
let x = new Node('x');
let y = new Node('y');
let z = new Node('z');
w.right = x;
x.right = y;
y.right = z;


console.log(isBalanced(a));
console.log(isBalanced(w));
