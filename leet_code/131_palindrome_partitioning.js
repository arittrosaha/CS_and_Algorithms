// Given a string s, partition s such that every substring of the partition is a palindrome.
// Return all possible palindrome partitioning of s.

// Example:
// Input: "aab"
// Output:
// [
//     ["aa", "b"],
//     ["a", "a", "b"]
// ]

/**
 * @param {string} s
 * @return {string[][]}
 */

var partition = function (s, memo={}) {
    let key = s;
    if (key in memo) return memo[key];
    if (!s.length) return [[]];

    let results = [];
    for (let i = 0; i < s.length; i++) {
        let left = s.slice(0, i+1)
        if (palindrome(left)) {
            let right = s.slice(i+1);
            partition(right, memo).forEach(result => {
                results.push([left, ...result]);
            });
        }
    }

    memo[key] = results;
    return memo[key];
};

function palindrome (string) {
    for (let i = 0; i < Math.floor(string.length/2); i++) {
        if (string[i] !== string[string.length - (i + 1)]) {
            return false
        }
    }

    return true
}

console.log(partition("cdd"));