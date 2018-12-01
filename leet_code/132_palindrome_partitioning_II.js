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

var 3 = function (s) {
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


// Alvin's solution
var minCut2 = function (s, memo = { '': -1 }) {
    if (s in memo) return memo[s];

    let currMin = Infinity;

    for (let i = 0; i < s.length; i++) {
        let prefix = s.slice(0, i + 1);
        if (isPalindrome(prefix)) {
            let suffix = s.slice(i + 1);
            let cutAmt = 1 + minCut2(suffix, memo);
            if (cutAmt < currMin) currMin = cutAmt;
        }
    }

    memo[s] = currMin;
    return memo[s];
};


function isPalindrome(str) {
    for (let i = 0; i < str.length / 2; i++) {
        if (str[i] !== str[str.length - 1 - i]) return false;
    }

    return true;
}

// Chao's solution
var minCut3 = function (s) {
    let n = s.length;
    let cuts = new Array(n + 1);
    for (let i = 0; i <= n; i++) cuts[i] = i - 1;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j <= i && i + j < n && s[i - j] == s[i + j]; j++)
            cuts[i + j + 1] = Math.min(cuts[i + j + 1], 1 + cuts[i - j]);
        for (let j = 1; j - 1 <= i && i + j < n && s[i - j + 1] == s[i + j]; j++)
            cuts[i + j + 1] = Math.min(cuts[i + j + 1], 1 + cuts[i - j + 1]);
    }
    return cuts[n];
}