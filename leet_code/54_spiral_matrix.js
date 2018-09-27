// Given a matrix of m x n elements (m rows, n columns), return all elements
//  of the matrix in spiral order.
//
// Example 1:
//
// Input:
// [
//  [ 1, 2, 3 ],
//  [ 4, 5, 6 ],
//  [ 7, 8, 9 ]
// ]
// Output: [1,2,3,6,9,8,7,4,5]
// Example 2:
//
// Input:
// [
//   [1, 2, 3, 4],
//   [5, 6, 7, 8],
//   [9,10,11,12]
// ]
// Output: [1,2,3,4,8,12,11,10,9,5,6,7]
//
// /**
//  * @param {number[][]} matrix
//  * @return {number[]}
//  */

var spiralOrder = function(matrix) {
  let vals = [];

  for (let col = 0; col < matrix[0].length - 1; col++) vals.push(matrix[0][col]);
  for (let row = 0; row < matrix.length - 1; row++) vals.push(matrix[row][matrix[0].length - 1]);
  for (let col = matrix[0].length - 1; col > 0; col--) vals.push(matrix[matrix.length-1][col]);
  for (let row = matrix.length - 1; row > 0; row++) vals.push(matrix[row][0]);

  let newMatrix = [];

};
