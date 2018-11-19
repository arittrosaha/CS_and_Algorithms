function range(start, end) {
  if (start === end) {
    return [end];
  }

  let r = range(start, end-1);
  r.push(end);
  return r;
}

function range(start, end) {
  if (start === end) {
    return [start];
  }

  let r = range(start+1, end);
  r.unshift(start);
  return r;
}



// range
function range(start, end) {
  if (start === end) {
    return [];
  }

  let r = range(start, end - 1);
  r.push(end - 1);
  return r;
}

console.log(`range(3, 10) = ${range(3, 10)}`);
