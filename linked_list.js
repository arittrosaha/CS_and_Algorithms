class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class LL {
  constructor() {
    this.head = null;
  }

  insert(val, node = this.head) {
    if (!this.head) {
      this.head = new Node(val);
      return;
    }
    if (!node.next) {
      node.next = new Node(val);
    } else {
      this.insert(val, node.next);
    }
  }

  delete(idx, node = this.head, pos = 0) {
    if (idx === pos + 1) { // if we are the parent of the target node
      node.next = node.next.next;
    } else {
      this.delete(idx, node.next, pos + 1);
    }
  }

  reverse(node = this.head, prev = null) {
    if (!node.next) {
      this.head = node;
      node.next = prev;   // if I am at the tail, then return tail
      return node;
    } else {
      let newHead = this.reverse(node.next, node);
      node.next = prev;
      return newHead;
    }
  }

  print(node = this.head) {
    if (!node) {
      return;
    }
    console.log(node.val);
    this.print(node.next);
  }
}

let list = new LL();
list.insert("a");
list.insert("b");
list.insert("c");
list.insert("d");
list.print();
list.reverse();
list.print();
list.delete(2); // this should delete b (after reverse)
list.print();
