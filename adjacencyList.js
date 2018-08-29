let neighbors = {
  'a': new Set(['b', 'c']),
  'b': new Set(['g']),
  'z': new Set([]),
  'c': new Set(['b', 'd']),
  'd': new Set(),
  'e': new Set(['f']),
  'f': new Set(),
  'g': new Set(),
};

function DFS(neighbors) {
  let visited = new Set();

  for (let node in neighbors) {
    _DFS(neighbors, node, visited);
  }
}

function _DFS(neighbors, curr, visited) {
  if (visited.has(curr)) return;
  visited.add(curr);
  console.log(curr);

  // doing depth first order
  for (let node of neighbors[curr]) {
    _DFS(neighbors, node, visited);
  }
}

DFS(neighbors);
