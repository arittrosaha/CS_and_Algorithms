// Write an Array#merge_sort method; it should not modify the original array.


Array.prototype.mergeSort = function () {
  if (this.length <= 1) {
    return this;
  }

  let middle = Math.floor(this.length/2);
  let left = this.slice(0,middle);
  let right = this.slice(middle);

  let leftsort = left.mergeSort();
  let rightsort = right.mergeSort();

  return merge (leftsort, rightsort);
};

function merge (left, right) {
  let merged = [];

  while (left.length !== 0 && right.length !== 0) {
    if (left[0] < right[0]) {
      merged.push(left.shift());
    } else if (left[0] > right[0]) {
      merged.push(right.shift());
    } else if (left[0] === right [0]) {
      merged.push(left.shift());
    }
  }
  return merged.concat(left).concat(right);
}


function mergeSort = function (array) {
  if array.length === 1 return array;

  let middle = Math.floor(array.length/2)

  let left = mergeSort(array.slice(0, middle));
  let right = mergeSort(array.slice(middle));

  return merge(left, right);
};

function merge = function (left, right) {
  let merged = []
  while (left.length > 0 && right.length > 0) {
    let nextItem = left[0] < right[0] ? left.shift() : right.shift();
    merged.push(nextItem);
  };
  return merged.concat(left).concat(right);
};









// merge, mergeSort
function merge(left, right) {
  const merged = [];

  while (left.length > 0 && right.length > 0) {
    let nextItem = (left[0] < right[0]) ? left.shift() : right.shift();
    merged.push(nextItem);
  }

  return merged.concat(left, right);
}

function mergeSort(array) {
  if (array.length < 2) {
    return array;
  } else {
    const middle = Math.floor(array.length / 2);

    const left = mergeSort(array.slice(0, middle));
    const right = mergeSort(array.slice(middle));

    return merge(left, right);
  }
}

console.log(`mergeSort([4, 5, 2, 3, 1]) = ${mergeSort([4, 5, 2, 3, 1])}`);

Array.prototype.mergeSort = function (func) {
  if (this.length <= 1) return this;

  if (!func) func = (left,  right) => {
    return left < right ? -1 : left > right ? 1 : 0;
  }

  const midpoint = Math.floor(this.length / 2);
  const sortedLeft = this.slice(0, midpoint).mergeSort(func);
  const sortedRight = this.slice(midpoint).mergeSort(func);

  return sortedLeft.merge(sortedRight, func);
}

Array.prototype.merge = function (arr, func) {
  let merged = [];

  while (this.length && arr.length) {
    switch(func(this[0], arr[0])) {
      case -1:
        merged.push(this.shift());
        break
      case 0:
        merged.push(this.shift());
        break
      case 1:
        merged.push(arr.shift());
        break
    }
  }

  merged = merged.concat(this);
  merged = merged.concat(arr);

  return merged;
}
