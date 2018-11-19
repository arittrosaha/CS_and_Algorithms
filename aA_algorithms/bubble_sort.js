Array.prototype.bubbleSort = function (comparator) {
  if (typeof comparator === "undefined") {
    comparator = function (a, b) {
      if (a < b) {
        return -1;
      } else if ( a === b ) {
        return 0;
      } else {
        return 1;
      }
    };
  }

  var sorted = false;

  while (!sorted) {
    sorted = true;

    for (var i = 0; i < this.length-1; i++) {
      let current = this[i];
      let next = this[i+1];

      if (comparator(current, next) === 1) {
        this[i] = next;
        this[i+1] = current;
        sorted = false;
      }
    }
  }

  return this;
};



Array.prototype.bubbleSort = function (func) {
  let sorted = false;

  while(!sorted) {
    let sorted = true;

    for (var i = 0; i < this.length; i++) {
      if (this[i] > this[i+1]) {
        let temp = this[i];
        this[i] = this[i+1];
        this[i+1] = temp;
        sorted = false;
      };
    };
  };

  return this
};

// Array#bubbleSort
Array.prototype.bubbleSort = function () {
  let isSorted = false;

  while (!isSorted) {
    isSorted = true;

    for (let i = 0; i < (this.length - 1); i++) {
      if (this[i] > this[i + 1]) {
        // a crafty bit of array destructuring to avoid a temp variable
        [this[i], this[i + 1]] = [this[i + 1], this[i]];
        isSorted = false;
      }
    }
  }

  return this;
};

console.log([5, 3, 4, 2, 1].bubbleSort());

Array.prototype.bubbleSort = function(func) {
  let sorted = false;

  if (!func) {
    func = (x, y) => {
      if (x <= y) return -1;
      return 1;
    }
  }

  while (!sorted) {
    sorted = true;
    for (let i = 0; i < this.length; i++) {
      if (i + 1 === this.length) continue;

      if (func(this[i], this[i + 1]) === 1) {
        sorted = false;
        let current = this[i], next = this[i + 1];
        this[i] = next, this[i + 1] = current;
      }
    }
  }

  return this;
}
