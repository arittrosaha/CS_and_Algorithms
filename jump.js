function jumpSlow(nums, idx = 0) { // O(n) : n!
  if (idx === nums.length - 1) return 0;
  if (idx > nums.length - 1) return nums.length;
  
  let max = nums[idx];
  let ways = [];
  for (let i = 1; i <= max; i++) {
    ways.push(jumpSlow(nums, idx + i) + 1);
  }
 return Math.min(...ways);
}

function jumpFast(nums, idx = 0, memo = {}) {
  if (idx in memo) return memo[idx];
  if (idx === nums.length - 1) return 0;
  if (idx > nums.length - 1) return nums.length;

  let max = nums[idx];
  let ways = [];
  for (let i = 1; i <= max; i++) {
    ways.push(jumpFast(nums, idx + i, memo) + 1);
  }
  memo[idx] = Math.min(...ways);
  return memo[idx];
}

let input = [2,3,1,1,4]; // => 2
console.log(jumpSlow(input));
console.log(jumpFast(input));
