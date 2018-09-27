// A message containing letters from A-Z is being encoded to numbers using the following mapping:
//
// 'A' -> 1
// 'B' -> 2
// ...
// 'Z' -> 26
// Given a non-empty string containing only digits, determine the total number of ways to decode it.
//
// Example 1:
//
// Input: "12"
// Output: 2
// Explanation: It could be decoded as "AB" (1 2) or "L" (12).
// Example 2:
//
// Input: "226"
// Output: 3
// Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
//
// /**
//  * @param {string} s
//  * @return {number}
//  */
//

var numDecodings = function(s, m = {}) {
  if (s in memo) return memo[s];
  if (s[0] === "0") return 0;
  if (s.length <= 1) return 1;

  let numWays = 0;

  numWays += numDecodings(s.slice(1), m);

  if (Number(s.slice(0,2)) <= 26) {
    numWays += numDecodings(s.slice(2), m);
  }

  memo[s] = numWays;
  return memo[s];
};
