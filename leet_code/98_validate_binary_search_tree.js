class Node {
  constructor(val) {
    this.val = val;
    this.left = this.right = null;
  }
}

var isValidBST = function(root) {
  if (!root) return true;

  let leftVal = root.left ? root.left.val : Infinity;
  let rightVal = root.right ? root.right.val : -Infinity;

  let isRootGood = (leftVal < root.val) && (rightVal > root.val);
  let areSubTreesGood = isValidBST(root.left) && isValidBST(root.right);

  return isRootGood && areSubTreesGood;
};
