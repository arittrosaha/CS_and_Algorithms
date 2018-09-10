// Given a m x n grid filled with non-negative numbers, find a path from
// top left to bottom right which minimizes the sum of all numbers along its path.

// Note: You can only move either down or right at any point in time.

// Example:

// Input:
// [
//   [1,3,1],
//   [1,5,1],
//   [4,2,1]
// ]
// Output: 7
// Explanation: Because the path 1→3→1→1→1 minimizes the sum.

var minPathSum1 = function(grid) {
    for(let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (i === 0 && j === 0) {
                continue;
            } else if (i === 0) {
              grid[i][j] += grid[i][j-1];
            } else if (j === 0) {
              grid[i][j] += grid[i-1][j];
            }
            else {
                grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1]);
            }
        }
    }
    return grid[grid.length-1][grid[0].length-1];
};

console.log(minPathSum1([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]));

// memo = { row, col: shortest path sum from 0,0 to row, col }

function treverse(grid, row=0, col=0) {
  if (row === grid.length || col === grid[0].length) return;
  console.log(grid[row][col]);
  treverse(grid, row, col + 1);
  treverse(grid, row + 1, col);
}

function minPathSum2(grid, row=0, col=0, memo = {}) {
  let key = `${row}-${col}`;

  // if my pos is invalid
  if (row >= grid.length || col >= grid[0].length) return Infinity;
  // if my pos is already at goal
  if (row === grid.length - 1 && col === grid[0].length - 1) return grid[row][col];

  if (key in memo) {
    return memo[key];
  }

  let result = grid[row][col] + Math.min(
    minPathSum2(grid, row + 1, col),
    minPathSum2(grid, row, col + 1)
  );

  // if Infinity was not used, then use the following code:

  // let down = minPathSum2(grid, row + 1, col, memo);
  // let right = minPathSum2(grid, row, col + 1, memo);
  //
  // let result;
  // if (right === null) {
  //   result = grid[row][col] + down;
  // } else if (down === null) {
  //   result = grid[row][col] + right;
  // } else {
  //   result = grid[row][col] + Math.min(
  //     minPathSum2(grid, row + 1, col),
  //     minPathSum2(grid, row, col + 1)
  //   );
  // }

  memo[key] =result;
  return memo[key];
}
