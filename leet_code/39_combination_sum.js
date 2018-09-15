// Given a set of candidate numbers (candidates) (without duplicates) and a
// target number (target), find all unique combinations in candidates where
// the candidate numbers sums to target.

// The same repeated number may be chosen from candidates unlimited number of times.

// Note:

// All numbers (including target) will be positive integers.
// The solution set must not contain duplicate combinations.
// Example 1:

// Input: candidates = [2,3,6,7], target = 7,
// A solution set is:
// [
//   [7],
//   [2,2,3]
// ]
// Example 2:

// Input: candidates = [2,3,5], target = 8,
// A solution set is:
// [
//   [2,2,2,2],
//   [2,3,3],
//   [3,5]
// ]

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */

// var combinationSum = function(candidates, target) {
//     if (target === 0) return [[]];
//     if (target < 0) return [];
//
//     let allCombinations = [];
//
//     candidates.forEach((candidate) => {
//       allCombinations.push(...combinationSum(candidates, target - candidate).map((combination) => [candidate, ...combination]));
//     });
//
//     return allCombinations;
// };

var combinationSum = function(candidates, target) {
    if (target === 0) return [[]];
    if (target < 0 || !candidates.length) return [];

    let allCombinations = [];

    let cand = candidates[0];

    for (let num = 0; num <= target / cand; num++) {
        allCombinations.push(
          ...combinationSum(candidates.slice(1), target - (cand * num))
            .map((combination) => [...new Array(num).fill(cand), ...combination]));
    }

    return allCombinations;
};



console.log(combinationSum([2,3,6,7], 7));
