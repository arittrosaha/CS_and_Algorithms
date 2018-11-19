// Implement a method that finds the sum of the first n
// fibonacci numbers recursively. Assume n > 0

function fibsSum(n) {
  if (n===0) {return 0};
  if (n===1) {return 1};

  return fibsSum(n-2) + fibsSum(n-1) + 1;
}

function fibsSum(n) {
  if (n === 0) return 0;
  if (n === 1) return 1;

  return fibsSum(n - 1) + fibsSum(n - 2) + 1;
}
