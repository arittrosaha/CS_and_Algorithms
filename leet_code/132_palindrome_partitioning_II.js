// Given a string s, partition s such that every substring of the partition is a palindrome.

// Return the minimum cuts needed for a palindrome partitioning of s.

// Example:
// Input: "aab"
// Output: 1
// Explanation: The palindrome partitioning["aa", "b"] could be produced using 1 cut.

/**
 * @param {string} s
 * @return {number}
 */

var minCut = function (s) {
    return (minPartition(s).length - 1);
};

function minPartition (s, memo = {}) {
    let key = s;
    if (key in memo) return memo[key];
    if (!s.length) return [];

    let smallestLength = Infinity;
    let result;
    for (let i = 0; i < s.length; i++) {
        let left = s.slice(0, i + 1)
        if (isPalindrome(left)) {
            let newResult = [left, ...minPartition(s.slice(i + 1), memo)];
            let newResultLength = newResult.length;
            if (newResultLength < smallestLength) {
                smallestLength = newResultLength;
                result = newResult;
            }
        }
    }

    memo[key] = result;
    return memo[key];
};

function isPalindrome (string) {
    for (let i = 0; i < Math.floor(string.length/2); i++) {
        let current = string[i];
        let reciprocal = string[string.length - (i+1)];
        if (current !== reciprocal) {
            return false;
        }
    }

    return true;
}

console.log(minPartition("aab"))