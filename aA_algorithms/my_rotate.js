Array.prototype.rotate = function (num) {
  let offset = num % this.length;
  let rotated = this.slice(offset).concat(this.slice(0, offset));
  return rotated;
};


Array.prototype.rotate = function (times = 1) {
  let rotations;
  const rotated = this.slice(0);

  if (times < 0) rotations = this.length % (Math.abs(times) / this.length);
  else rotations = times % this.length;

  for (let i = 0; i < rotations; i++) {
    rotated.push(rotated.shift());
  }

  return rotated;
};
