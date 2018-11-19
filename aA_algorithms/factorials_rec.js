// Write a recursive method that returns the first "num" factorial numbers.
// Note that the 1st factorial number is 0!, which equals 1. The 2nd factorial
// is 1!, the 3rd factorial is 2!, etc.


function factorialsRec(num) {
  if (num === 1) return [1];

  const facs = factorialsRec(num - 1);
  facs.push(facs[facs.length - 1] * (num - 1));
  return facs;
}

function factorials(num) {
  if (num === 0) return [1];

  let facs = factorialsRec(num-1);
  facs = facs * num;
  return facs;
}
