function jumpBF(nums, idx = 0) { // O(n) : n!
  if (idx === nums.length - 1) return 0;
  if (idx > nums.length - 1) return nums.length;

  let max = nums[idx];
  let ways = [];
  for (let i = 1; i <= max; i++) {
    ways.push(jumpBF(nums, idx + i) + 1);
  }
 return Math.min(...ways);
}

function jumpMemo(nums, idx = 0, memo = {}) {
  if (idx in memo) return memo[idx];
  if (idx === nums.length - 1) return 0;
  if (idx > nums.length - 1) return nums.length;

  let max = nums[idx];
  let ways = [];
  for (let i = 1; i <= max; i++) {
    ways.push(jumpMemo(nums, idx + i, memo) + 1);
  }

  memo[idx] = Math.min(...ways);
  return memo[idx];
}

let input = [2,3,1,1,4]; // => 2
console.log(jumpBF(input));
console.log(jumpMemo(input));

function jumpGraph(nums) {
  if (nums.length === 1) return 0;

  let stack = [ {index: 0, depth: 0} ];

  while (stack.length) {
    let node = stack.pop();

    let neighbors = getNeighborIndices(nums, node.index);
    for (let i = 0; i < neighbors.length; i++) {
      let neighborIdx = neighbors[i];
      let neighborDepth = node.depth + 1;
      if (neighborIdx === nums.length - 1) return neighborDepth;
      stack.push({ index: neighborIdx, depth: neighborDepth });
    }
  }
}

function getNeighborIndices(nums, idx) {
  let neighbors = [];

  for (let i = 1; i <= nums[idx]; i++) {
    neighbors.push(idx + i);
  }

  return neighbors.sort((a, b) => (nums[a] + a - idx) - (nums[b] + b - idx));
}

var jumpLC = function(nums) {
    let jumps = 0, currEnd = 0, currFarthest = 0;

    for (let i = 0; i < nums.length-1; i++) {
        currFarthest = Math.max(currFarthest, nums[i] + i);

        if (currFarthest >= nums.length-1) {
            jumps++;
            break;
        }
        if (i === currEnd) {
            jumps++;
            currEnd = currFarthest;
        }
    }
    return jumps;
};
