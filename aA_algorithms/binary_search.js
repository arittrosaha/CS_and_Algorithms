// # Write a monkey patch of binary search:
// # E.g. [1, 2, 3, 4, 5, 7].my_bsearch(5) => 4

Array.prototype.myBsearch = function (target) {
  if (this.length === 0) {
    return -1;
  }

  var middle = Math.floor(this.length/2);
  var left = this.slice(0, middle);
  var right = this.slice(middle+1);

  if (target < this[middle]) {
    return left.myBsearch(target);
  } else if (target === this[middle]) {
    return middle;
  } else {
    let sub = right.myBsearch(target);
    return sub === -1 ? sub : ((middle+1) + sub);
  }
};











Array.prototype.myBsearch = function (numbers, target) {
  if (numbers.length === 0) {
    return -1
  }

  const middle = Math.floor(numbers.length/2)

  if (numbers[middle] > target) {
    const left = numbers.slice(0,middle)
    return myBsearch(left , target)
  } else if (numbers[middle] === target) {
    return middle
  } else {
    const right = numbers.slice(middle+1)
    const subProblem = myBsearch(right , target)

    return subProblem === -1 ? -1 : (subProblem + (middle+1));
  }



}

// bsearch
function bsearch(numbers, target) {
  if (numbers.length === 0) {
    return -1;
  }

  const probeIdx = Math.floor(numbers.length / 2);
  const probe = numbers[probeIdx];

  if (target === probe) {
    return probeIdx;
  } else if (target < probe) {
    const left = numbers.slice(0, probeIdx);
    return bsearch(left, target);
  } else {
    const right = numbers.slice(probeIdx + 1);
    const subProblem = bsearch(right, target);

    return subProblem === -1 ? -1 : subProblem + (probeIdx + 1);
  }
}

console.log(`bsearch([1, 2, 3], 3) = ${bsearch([1, 2, 3], 3)}`);
console.log(`bsearch([1, 2, 3], 2.5) = ${bsearch([1, 2, 3], 2.5)}`);

Array.prototype.myBsearch = function(target, func) {
  if (this.length === 0) return null;
  const mid = Math.floor(this.length / 2);

  if (this[mid] === target) {
    return mid;
  } else if (this[mid] > target) {
    return this.slice(0, mid).myBsearch(target);
  } else {
    const result = this.slice(mid + 1, this.length).myBsearch(target);
    return result === null ? result : mid + 1 + result
  }
}
