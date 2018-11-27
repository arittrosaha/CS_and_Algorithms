// Given a non - empty string s and a dictionary wordDict containing a list of non - empty words, 
// determine if s can be segmented into a space - separated sequence of one or more dictionary words.

// Note:
// - The same word in the dictionary may be reused multiple times in the segmentation.
// - You may assume the dictionary does not contain duplicate words.

// Example 1:
// Input: s = "leetcode", wordDict = ["leet", "code"]
// Output: true
// Explanation: Return true because "leetcode" can be segmented as "leet code".

// Example 2:
// Input: s = "applepenapple", wordDict = ["apple", "pen"]
// Output: true
// Explanation: Return true because "applepenapple" can be segmented as "apple pen apple". Note that 
// you are allowed to reuse a dictionary word.

// Example 3:
// Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
// Output: false

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */

// Alvin's solution
var wordBreak = function (s, wordDict) {
    let explored = new Set();
    let markers = [-1];
    let lastPos = s.length - 1;
    while (markers.length) {
        let currPos = markers.shift();

        if (explored.has(currPos)) continue;

        for (let i = currPos + 1; i < s.length; i++) {
            let prefix = s.slice(currPos + 1, i + 1);
            if (wordDict.includes(prefix)) {
                markers.push(i);
                if (i === lastPos) return true;
            }
        }

        explored.add(currPos);
    }
    return false;
};