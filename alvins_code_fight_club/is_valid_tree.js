class Node {
  constructor(val) {
    this.val = val;
    this.left = this.right = null;
  }
}

function isValidBST(root) {
  let arr = [];
  inOrderTraverse(root, arr);
  return arr.join(',') === arr.sort((a, b) => a - b).join(',');
}

function inOrderTraverse(root, arr) {
  if (!root) return;
  inOrderPrint(root.left);
  arr.push(root.val);
  inOrderPrint(root.right);
}
