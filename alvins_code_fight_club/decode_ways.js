var numDecodings = function(s, memo = {}) {
    if (s in memo) return memo[s];
    if (s[0] === '0') return 0;
    if (s.length <= 1) return 1;

    let numWays = 0;

    numWays += numDecodings(s.slice(1), memo);

    if (Number(s.slice(0, 2)) <= 26) {
        numWays += numDecodings(s.slice(2), memo);
    }

    memo[s] = numWays;
    return memo[s];
};

// How to Memoize
// 1. Find brute force
// 2. add memo obj to parameters (arg : return value pairs)
// 3. at the VERY TOP of your function, check if arg is in your memo
// 4. RIGHT BEFORE you return, save that return val into the memo, using your arg
