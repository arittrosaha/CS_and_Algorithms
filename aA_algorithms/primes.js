// primes(num) returns an array of the first "num" primes.
// You may wish to use an is_prime helper method.

function primes(num) {
  let primeNums = [];

  for (var i = 2; primeNums.length < num; i++) {
    if (isPrime(i)) {
      primeNums.push(i);
    }
  }

return primeNums;
}

function sumNPrimes(num) {
  let primeNums = [];
  let sum = 0;

  for (var i = 2; primeNums.length < num; i++) {
    if (isPrime(i)) {
      primeNums.push(i);
      sum += i;
    }
  }

return sum;
}

function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  for (var i = 2; i < num; i++) {
    if ((num % i) === 0) {
      return false;
    }
  }

  return true;
}


function primes(count) {
  const primes = [];
  let i = 2;

  const isPrime = (num) => {
    for (var i = 2; i < num; i++) {
      if (num % i === 0) return false;
    }

    return true;
  }

  while (primes.length < count) {
    if (isPrime(i)) primes.push(i);
    i += 1;
  }

  return primes;
}

// write sumNPrimes(n)
function sumNPrimes (n) {
  let i = 1;
  let count = 0;
  let sum = 0;

  while (count < n) {
    if (isPrime(i)) {
      count += 1;
      sum += i;
    }
    i += 1;
  }

  return sum;
}

const isPrime = (num) => {
  if (num <= 1) { return false; }

  for (let i = 2; i < num; i++) {
    if (num % i === 0) {
      return false;
    }
  }

  return true;
};
