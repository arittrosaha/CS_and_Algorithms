// Given two integers n and k, return all possible combinations of k numbers
// out of 1 ... n.
//
// Example:
//
// Input: n = 4, k = 2
// Output:
// [
//   [2,4],
//   [3,4],
//   [2,3],
//   [1,2],
//   [1,3],
//   [1,4],
// ]
//
// /**
//  * @param {number} n
//  * @param {number} k
//  * @return {number[][]}
//  */

var combine = function(n, k) {
  if (k === 0) return [[]];
  if (n < k) return [];

  return [...combine(n-1, k-1).map(c => [n, ...c]),...combine(n-1,k)];
};

console.log(combine(4, 2));
