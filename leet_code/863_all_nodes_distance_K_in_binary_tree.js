// We are given a binary tree(with root node root), a target node, and an integer value K.
// Return a list of the values of all nodes that have a distance K from the target node.The answer can be returned in any order.

// Example 1:
// Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], target = 5, K = 2
// Output: [7, 4, 1]

// Explanation:
// The nodes that are a distance 2 from the target node(with value 5)
// have values 7, 4, and 1. 

// Note that the inputs "root" and "target" are actually TreeNodes.
// The descriptions of the inputs above are just serializations of these objects.


// Note:
// - The given tree is non - empty.
// - Each node in the tree has unique values 0 <= node.val <= 500.
// - The target node is a node in the tree.
// - 0 <= K <= 1000.

// Dan's solution


var distanceK1 = function (root, target, K) {
    if (K === 0) return [target.val];
    const answers = [];
    addParent(root);
    const targetNode = findTarget(root, target);
    if (!targetNode) return [];
    findKNodesAwayDown(targetNode, K, answers);
    if (targetNode.val !== root.val) findKNodesAwayUp(targetNode, K, answers);
    return answers;
};

function addParent(root, parent) {
    // console.log(root);
    if (!root) return;
    if (parent) root.parent = parent;
    addParent(root.left, root);
    addParent(root.right, root);
}

function findTarget(root, target) {
    if (!root) return null;
    if (root.val === target.val) return root;

    return findTarget(root.left, target) || findTarget(root.right, target);
}

function findKNodesAwayDown(root, k, answers) {
    if (!root) return;
    if (k === 0) answers.push(root.val);
    findKNodesAwayDown(root.left, k - 1, answers);
    findKNodesAwayDown(root.right, k - 1, answers);
}

function findKNodesAwayUp(root, k, answers, prevNode) {
    if (k === 0) answers.push(root.val);
    if (root.parent === undefined) {
        if (prevNode === undefined) {
            findKNodesAwayDown(root.left, k - 1, answers);
            findKNodesAwayDown(root.right, k - 1, answers);
        } else if (root.left && prevNode.val !== root.left.val) {
            findKNodesAwayDown(root.left, k - 1, answers);
        } else if (root.right && prevNode.val !== root.right.val) {
            findKNodesAwayDown(root.right, k - 1, answers);
        }
        return;
    }
    if (prevNode) {
        if (root.left && prevNode.val !== root.left.val)
            findKNodesAwayDown(root.left, k - 1, answers);
        if (root.right && prevNode.val !== root.right.val)
            findKNodesAwayDown(root.right, k - 1, answers);
    }
    findKNodesAwayUp(root.parent, k - 1, answers, root);
}

// Alvin's Solution

// ancestors of a target are nodes that lie in the path above the target
// descendents of a target are nodes that lie in a path below the target

function distanceK(root, target, K) {
    let visited = new Set();

    // get all ancestors of the target
    let path = findPathToTarget(root, target);
    let pathVals = path.map((node) => node.val);

    // get values at distance K that are descendents the target at distance
    let answers = childrenAtDistance(target, K, visited);

    // get values at distance K that are inherited through ancestors of the target
    answers.push(
        ...path
            .reduce((acc, node, idx) => [...acc, ...childrenAtDistance(node, K - idx, visited)], [])
            .filter((val) => !pathVals.includes(val))
    );

    // there is guaranteed to be only one ancestor node at distance K
    if (pathVals.length > K && K !== 0) answers.push(pathVals[K]);

    return answers;
}

// returns an array containing the nodes along the path from the absolute root to the target
// returns null if the subtree does not contain the target
function findPathToTarget(root, target) {
    if (!root) return null;
    if (root === target) return [root];
    let path = findPathToTarget(root.left, target) || findPathToTarget(root.right, target);
    return path ? [...path, root] : null;
}


// return an array of all descendant node values that are `distance` edges away,
// visited is tracked to avoid explored duplicate values
function childrenAtDistance(root, distance, visited) {
    if (!root || distance < 0 || visited.has(root)) return [];
    visited.add(root);

    if (distance === 0) return [root.val];

    return [
        ...childrenAtDistance(root.left, distance - 1, visited),
        ...childrenAtDistance(root.right, distance - 1, visited)
    ];
}