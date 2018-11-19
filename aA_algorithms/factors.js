// Write a method that returns the factors of a number in ascending order.

function factors(num) {
  const factors = []

  for (var i = 2; i < num; i++) {
    if ((num % i) === 0) {
      factors.push(i);
    };
  };

  return factors;
};


function factors(num) {
  let factors = Array.from(Array(num)).map( (el, idx) => idx + 1)
  return factors.filter( el => num % el === 0);
}
