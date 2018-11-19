// Write a recursive function that returns the prime factorization of
// a given number. Assume num > 1
//
// prime_factorization(12) => [2,2,3]



function primeFactorization(num) {
  if (num === 1) return [];

  for (let i = 2; i < num; i++) {
    if (num % i === 0) {
      let factors = [i].concat(primeFactorization(Math.floor(num / i)));
      return factors;
    }
  }

  return [num];
}
