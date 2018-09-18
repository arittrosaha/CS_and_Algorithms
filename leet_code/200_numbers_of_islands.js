// Given a 2d grid map of '1's (land) and '0's (water), count the number of
//  islands. An island is surrounded by water and is formed by connecting
//  adjacent lands horizontally or vertically. You may assume all four edges
//  of the grid are all surrounded by water.
//
// Example 1:
//
// Input:
// 11110
// 11010
// 11000
// 00000
//
// Output: 1
// Example 2:
//
// Input:
// 11000
// 11000
// 00100
// 00011
//
// Output: 3

// /**
//  * @param {character[][]} grid
//  * @return {number}
//  */
var numIslands = function(grid) {
  let counter = 0;
  for(let row = 0; row < grid.length; row++) {
    for (let col = 0; col < grid[0].length; col++) {
      if (grid[row][col] === "1") {
        search(grid, row, col);
        counter += 1;
      }
    }
  }
  return counter;
};


function search(grid, row, col) {
  if (row < 0 || row >= grid.length || col < 0 || col >= grid[0].length) return;
  if(grid[row][col] === "0" || grid[row][col] === "*") return;

  grid[row][col] = "*";

  search(grid, row-1, col);
  search(grid, row+1, col);
  search(grid, row, col-1);
  search(grid, row, col+1);
}
