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

function inverse(neighbors) {
  let inverseObj = {};

  Object.keys(neighbors).forEach((node) => {
    inverseObj[node] = new Set();
  });

  for (let parent in neighbors) {
    for (let child of neighbors[parent]) {
      inverseObj[child].add(parent);
    }
  }
  return inverseObj;
}

console.log(inverse(neighbors));

function topSort(neighbors) {
  let children = inverse(neighbors);
  let unvisited = new Set(Object.keys(children));
  let order = [];

  while (unvisited.size > 0) {
    for (let node in unvisited) {
      // if the node is not visited yet and it's parents have all been visited
      if (Array.from(children[node]).every((p) => !unvisited.has(p))) {
        unvisited.delete(node);
        order.push(node);
      }
    }
  }

  // console.log(order);
}

topSort(neighbors);
