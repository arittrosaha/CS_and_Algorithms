class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  insert(val, node = this.root) {
    if (!this.root) {
      this.root = new Node(val);
      return;
    }
    if (val < node.val) {
      if (node.left) {
        this.insert(val, node.left);
      } else {
        node.left = new Node(val);
      }
    } else {
      if (node.right) {
        this.insert(val, node.right);
      } else {
        node.right = new Node(val);
      }
    }
  }

  inorder(node = this.root){
    if (!node) return;
    this.inorder(node.left);
    console.log(node.val);
    this.inorder(node.right);
  }

// time = O(n)
// space = O(n)
  dFirst1() {  // iteratively
    let stack = [this.root];
    while (stack.length) {
      let top = stack.pop();
      console.log(top.val);
      if (top.right) stack.push(top.right);
      if (top.left) stack.push(top.left);
    }
  }

// time = O(n)
// space = O(n)
  dFirst2(node = this.root) {  // recursively
    if (!node) return;
    console.log(node.val);
    this.dFirst2(node.left);
    this.dFirst2(node.right);
  }

// time = O(n)
// space = O(n)
  bFirst() {  // iteratively
    let que = [this.root];
    while (que.length) {
      let front = que.shift();
      console.log(front.val);
      if (front.left) {
        que.push(front.left);
      }
      if (front.right) {
        que.push(front.right);
      }
    }
  }

}

const tree = new BST();
tree.insert(10);
tree.insert(5);
tree.insert(15);
tree.insert(16);
tree.insert(13);
tree.insert(4);
tree.insert(7);
tree.bFirst();
// tree.inorder(); // # => 5, 10, 13, 15, 16
// tree.dFirst1(); // # => 10, 5, 15, 13, 16
// tree.dFirst2(); // # => 10, 5, 15, 13, 16





// const ten = new Node(10);
// const five = new Node(5);
// const fift = new Node(15);
// const sixt = new Node(16);
// const thirt = new Node(13);
//
// ten.left = five;
// ten.right = fift;
// fift.left = thirt;
// fift.right = sixt;
//
// function inorder(node){
//   if (!node) return;
//   node.inorder(node.left);
//   console.log(node.val);
//   node.inorder(node.right);
// }
//
// inorder(ten);
