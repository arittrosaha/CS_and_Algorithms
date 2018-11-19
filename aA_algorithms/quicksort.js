// Write a monkey patch of quick sort that accepts a callback

// write Array.prototype.quickSort(comparator). Here's a quick refresher if
// you've forgotten how quickSort works:
//   - choose a pivot element from the array (usually the first)
//   - for each remaining element of the array:
//     - if the element is less than the pivot, put it in the left half of the
//     array.
//     - otherwise, put it in the right half of the array.
//   - recursively call quickSort on the left and right halves, and return the
//   full sorted array.


Array.prototype.quickSort = function (comparator) {
  if (this.length <= 1) {
    return this;
  }

  if (typeof comparator !== "function") {
    comparator = function (a, b) {
      if (a < b) {
        return -1;
      } else if (a > b) {
        return 1;
      } else if (a === b) {
        return 0;
      }
    };
  }

  let pivot = this[0];

  let left = this.slice(1).filter( el => comparator(el, pivot) === -1);
  let right = this.slice(1).filter( el => comparator(el, pivot) >= 0);

  return left.quickSort(comparator).concat([pivot]).concat(right.quickSort(comparator));
};














Array.prototype.quickSort = function (comparator) {
  if (this.length <= 1)  {
    return this;
  }

  if (typeof comparator !== 'function') {
    comparator = function (a, b) {
      if (a < b) {
        return -1;
      } else {
        return 1;
      }
    };
  }

  let pivot = this[0];
  let left = this.slice(1).filter( el => comparator(el, pivot) === -1);
  let right = this.slice(1).filter( el => comparator(el, pivot) > -1);

  left = left.quickSort(comparator);
  right = right.quickSort(comparator);

  return left.concat([pivot]).concat(right);
};











Array.prototype.quickSort = function (comparator) {
  if (this.length <= 1) return this;

  if (typeof comparator !== "function") {
    comparator = (x, y) => {
      if (x === y) {
        return 0;
      } else if (x < y) {
        return -1;
      } else {
        return 1;
      }
    };
  }

  const pivot = this[0];
  const left = [];
  const right = [];

  for (let i = 1; i < this.length; i++) {
    if (comparator(this[i], pivot) === -1) {
      left.push(this[i]);
    } else {
      right.push(this[i]);
    }
  }

  return left.quickSort(comparator).
    concat([pivot]).
    concat(right.quickSort(comparator));
};

Array.prototype.quickSort = function (func) {
  if (this.length < 2) return this;

  if (!func) {
    func = (x, y) => {
      if (x < y) return - 1;
      return 1;
    };
  }

  const pivot = this[0];
  let left = this.slice(1).filter( (el) => func(el, pivot) === -1);
  let right = this.slice(1).filter( (el) => func(el, pivot) != -1);
  left = left.quickSort(func);
  right = right.quickSort(func);

  return left.concat([pivot]).concat(right);
};
