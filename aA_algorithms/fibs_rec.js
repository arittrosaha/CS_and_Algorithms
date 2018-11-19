function fibsRec(n) {
  if (n === 2) {
    return [0,1].slice(0,n);
  };

  let fibs = fibsRec(n-1)
  fibs.push(fibs[fibs.length-1]+fibs[fibs.length-2]);
  return fibs;
}



// fibsRec, fibsIter
function fibsRec(n) {
  if (n < 3) {
    return [0, 1].slice(0, n);
  }

  let fibs = fibsRec(n - 1);
  fibs.push(fibs[fibs.length - 1] + fibs[fibs.length - 2]);

  return fibs;
}

console.log(`fibsRec(5) = ${fibsRec(5)}`);

function fibsIter(n) {
  let fibs = [0, 1];
  if (n < 3) {
    return fibs.slice(0, n);
  }

  while (fibs.length < n) {
    fibs.push(fibs[fibs.length - 2] + fibs[fibs.length - 1]);
  }

  return fibs;
}

console.log(`fibsIter(5) = ${fibsIter(5)}`);
