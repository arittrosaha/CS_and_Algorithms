var startTime, endTime;

function start() {
  startTime = new Date();
}

function end() {
  endTime = new Date();
  var timeDiff = endTime - startTime; //in ms
  // strip the ms

  // get seconds
  var seconds = Math.round(timeDiff);
  console.log(seconds + " ms");
}

function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

function makeLL(n) {
  if (n === 0) return null;
  let head = new TreeNode(n);
  head.right = makeLL(n - 1);
  return head;
}

function printLL(root) {
  if (!root) return;
  console.log(root.val);
  printLL(root.right);
}

let t = makeLL(10000);
start();
lowestCommonAncestor(t, 2, 1);
end();

// function lowestCommonAncestor(root, p, q) {
//     markDescendants(root, p.val);
//     markDescendants(root, q.val);
//     return _lowestCommonAncestor(root, p, q);
// }
//
// function _lowestCommonAncestor(root, p, q) {
//     if (!root) return null;
//     if (!(root[p.val] && root[q.val])) {
//         return null;
//     }
//
//     return _lowestCommonAncestor(root.left, p, q) || _lowestCommonAncestor(root.right, p, q) || root;
// }
//
// function markDescendants(root, val) {
//     if (!root) return false;
//     if (root.val === val) {
//         root[val] = true;
//         return true;
//     }
//     root[val] = markDescendants(root.left, val) || markDescendants(root.right, val);
//     return root[val];
// }


//
// function lowestCommonAncestor(root, p, q) {
//   let que = [root];
//   let lowestCommonAncestor;
//
//   let i = 0;
//   while (i < que.length) {
//     const node = que[i];
//     if (node.left) que.push(node.left);
//     if (node.right) que.push(node.right);
//
//     i += 1;
//   }
//
//   for (let i = que.length-1; i >= 0; i--) {
//     if (checkDescendentsDFS(que[i], p) && checkDescendentsDFS(que[i], q)) {
//       return que[i];
//     }
//   }
// };
//
// function checkDescendentsDFS(root, targetNode) {
//   if (!root) return null;
//   if (!targetNode) return null;
//   if (root.val === targetNode.val) return true;
//
//   if (checkDescendentsDFS(root.left, targetNode)) return true;
//   if (checkDescendentsDFS(root.right, targetNode)) return true;
//
//   return false;
// }

// function lowestCommonAncestor(root, p, q) {
//   if (!root) return new Set();
//
//   let left = lowestCommonAncestor(root.left, q, p);
//   if (left.val !== undefined) return left;
//   let right = lowestCommonAncestor(root.right, q, p);
//   if (right.val !== undefined) return right;
//
//   let combined = left;
//   for (let node of right) {
//     combined.add(node);
//   }
//
//   if (combined.has(p) && combined.has(q)) return root;
//   if (root === p && combined.has(q)) return root;
//   if (root === q && combined.has(p)) return root;
//
//   combined.add(root);
//   return combined;
// }

//
// function lowestCommonAncestor(root, p, q, memo={}) {
//   let que = [root];
//   let lowestCommonAncestor;
//
//   let i = 0;
//   while (i < que.length) {
//     const node = que[i];
//     if (node.left) que.push(node.left);
//     if (node.right) que.push(node.right);
//
//     i += 1;
//   }
//
//   for (let i = que.length-1; i >= 0; i--) {
//     if (checkDescendentsDFS(que[i], p, memo) && checkDescendentsDFS(que[i], q, memo)) {
//       return que[i];
//     }
//   }
// }
//
// function checkDescendentsDFS(root, targetNode, memo) {
//   if (!root) return null;
//   if (!targetNode) return null;
//   if (root.val === targetNode.val) return true;
//
//   let key = `${root.val}-${targetNode.val}`;
//   if (key in memo){
//       return memo[key];
//   }
//
//   if (checkDescendentsDFS(root.left, targetNode, memo)){
//     memo[key] = true;
//     return memo[key];
//   }
//   if (checkDescendentsDFS(root.right, targetNode, memo)) {
//     memo[key] = true;
//     return memo[key];
//   }
//   memo[key] = false;
//   return memo[key];
// }

function lowestCommonAncestor(root, p, q) {
  if (!root || root === p || root === q) return root;
  var resL = lowestCommonAncestor(root.left, p, q);
  var resR = lowestCommonAncestor(root.right, p, q);
  return (resL && resR) ? root : (resL || resR);
}



























//
