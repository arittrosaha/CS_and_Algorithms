class Node {
  constructor(val) {
    this.val = val;
    this.neighbors = [];
  }

}

function dfs(node, visited = new Set()){
  if (visited.has(node.val)) return [];
  visited.add(node.val);
  console.log(node.val);

  let otherNodes = [];
  node.neighbors.forEach((neighbor) => {
    otherNodes.push(...dfs(neighbor,visited));
  });

  return [node, ...otherNodes];
}

var a = new Node('a');
var b = new Node('b');
var c = new Node('c');
var d = new Node('d');

a.neighbors = [b, d];
b.neighbors = [c, d];
c.neighbors = [];
d.neighbors = [a, c];

dfs(a);
