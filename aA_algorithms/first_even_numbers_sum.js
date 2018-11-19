// return the sum of the first n even numbers recursively. Assume n > 0

function firstEvenNumbersSum(n) {
  if (n === 1) return 2;

  return 2 * n + firstEvenNumbersSum(n-1);
};

function firstEvenNumbersSum(n) {
  if (n === 1) return 2;
  return 2 * n + firstEvenNumbersSum(n - 1);
}
