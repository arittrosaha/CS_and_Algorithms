// How to Memoize (dynamic programming):

// 1. solve the brute force.

// 2. add a object as a param to the function obj should have
// param(s) : return val.

// 3. everywhere you return a value, add that value to the memo,
// using the param as the key.

// 4. at the very top, if memo contains param(s), return memo value.

function fibB(n) { // brute force; time - O(2^n); space: O(n)
  if (n === 1 || n === 2) {
    return 1;
  }

  return fibB(n - 1) + fibB(n - 2);
}

function fibM1(n, memo={}) { // Memoize v1; time: O(n); space: O(n)
  if (memo[n] !== undefined) {
    return memo[n];
  }

  if (n === 1 || n === 2) {
    return 1;
  }

  memo[n] = fibM1(n - 1, memo) + fibM1(n - 2, memo);
  return fibM1(n - 1) + fibM1(n - 2);
}

function fibM2(n, memo={1: 1, 2: 1}) {  // Memoize v2 (v1 simplified); time: O(n); space: O(n)
  if (n in memo) return memo[n];
  memo[n] = fibM2(n - 1, memo) + fibM2(n - 2, memo);
  return memo[n];
}

// tail call optimization would allow us to solve problems recursively in constant space.

function fibIter(n) {  // time: O(n); space: O(n)
  if (n === 1 || n === 2) {
    return 1;
  }

  let last = 1;
  let secondLast = 1;

  let i = 1;
  while(i < n) {
    var next = last + secondLast;

    secondLast = last;
    last = next;
    i++;
  }

  return next;
}
