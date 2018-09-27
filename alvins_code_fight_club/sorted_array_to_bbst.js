class Node {
  constructor(val) {
    this.val = val;
    this.left = this.right = null;
  }
}

function bbst(arr) {
  if (arr.length === 1) return new Node(arr[0]);
  if (arr.length === 0) return null;

  let middle = Math.floor(arr.length / 2);
  let node = new Node(arr[middle]);
  node.left = bbst(arr.slice(0, middle));
  node.right = bbst(arr.slice(middle + 1));
  return node;
}


function inOrderPrint(root) {
  if (!root) return;
  inOrderPrint(root.left);
  console.log(root.val);
  inOrderPrint(root.right);
}

function preOrderPrint(root) {
  if (!root) return;
  console.log(root.val);
  preOrderPrint(root.left);
  preOrderPrint(root.right);
}

function postOrderPrint(root) {
  if (!root) return;
  postOrderPrint(root.left);
  postOrderPrint(root.right);
  console.log(root.val);
}

let root = bbst([5, 10, 15, 20, 25, 30, 35]);
inOrderPrint(root);
console.log('-');
preOrderPrint(root);
console.log('-');
postOrderPrint(root);
