// Write a method that returns the median of elements in an array
// If the length is even, return the average of the middle two elements

Array.prototype.median = function () {
  let sorted = this.sort();
  if ((sorted.length % 2) === 0) {
    return (sorted[sorted.length/2] + sorted[(sorted.length/2)-1])/2;
  } else {
    return sorted[Math.floor(sorted.length/2)];
  }
};


Array.prototype.median = function () {
  if (!this.length) return null;
  const sorted = this.sort();
  const mid = Math.floor(this.length / 2);

  if (this.length % 2 !== 0) {
    return sorted[mid];
  } else {
    return (sorted[mid] + sorted[mid - 1]) / 2;
  }
};
