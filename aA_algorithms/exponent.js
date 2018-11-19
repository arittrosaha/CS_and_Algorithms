// return b^n recursively. Your solution should accept negative values
// for n


function exponent(b,n) {
  if (n > 0){
    return n === 0 ? 1 : b * exponent(b, n-1);
  } else {
    return n === 0 ? 1 : 1/b * exponent(b, n+1);
  }
}


// exp1, exp2
function exp1(base, exponent) {
  return exponent === 0 ? 1 : (base * exp1(base, exponent - 1));
}

console.log(`exp1(2, 4) = ${exp1(2, 4)}`);

function exp2(base, exponent) {
  if (exponent === 0) {
    return 1;
  }

  if (exponent % 2 === 0) {
    let subAnswer = exp2(base, exponent / 2);
    return subAnswer * subAnswer;
  } else {
    let subAnswer = exp2(base, ((exponent - 1) / 2));
    return subAnswer * subAnswer * base;
  }
}

console.log(`exp2(2, 4) =  ${exp2(2, 4)}`);
console.log(`exp2(2, 5) =  ${exp2(2, 5)}`);
