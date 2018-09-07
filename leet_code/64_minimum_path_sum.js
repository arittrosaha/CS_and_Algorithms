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

var minPathSum = function(grid) {

};

// memo = { row, col: shortest path sum from 0,0 to row, col }

function minPathSum1(grid, row=0, col=0) {
  if (row === grid.length || col === grid[0].length) return;
  console.log(grid[row][col]);
  minPathSum1(grid, row, col + 1);
  minPathSum1(grid, row + 1, col);
}
