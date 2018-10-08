// Given two words word1 and word2, find the minimum number of operations
// required to convert word1 to word2.
//
// You have the following 3 operations permitted on a word:
//
// Insert a character
// Delete a character
// Replace a character
// Example 1:
//
// Input: word1 = "horse", word2 = "ros"
// Output: 3
// Explanation:
// horse -> rorse (replace 'h' with 'r')
// rorse -> rose (remove 'r')
// rose -> ros (remove 'e')
// Example 2:
//
// Input: word1 = "intention", word2 = "execution"
// Output: 5
// Explanation:
// intention -> inention (remove 't')
// inention -> enention (replace 'i' with 'e')
// enention -> exention (replace 'n' with 'x')
// exention -> exection (replace 'n' with 'c')
// exection -> execution (insert 'u')

/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */

var minDistance = function(word1, word2) {
  if (word1 === word2) return 0;
  if (word1.length === 0) return word2.length;
  if (word2.length === 0) return word1.length;

  let options = [];

  for (var i = 0; i < word1.length; i++) {
    let slicedWord = word1.slice(0, i) + word1.slice(i + 1)
    options.push(1 + minDistance(slicedWord, word2))
  }

  for (var j = 0; j < word2.length; j++) {
    let slicedWord = word2.slice(0, j) + word2.slice(j + 1)
    options.push(1 + minDistance(word1, slicedWord))
  }

  for (var k = 0; k < word1.length; k++) {
    for (var l = 0; l < word2.length; l++) {
      let slicedWord1 = word1.slice(0, k) + word1.slice(k + 1);
      let slicedWord2 = word2.slice(0, l) + word2.slice(l + 1);
      options.push(1 + minDistance(slicedWord1, slicedWord2));
    }
  }

  return Math.min(...options);
};
