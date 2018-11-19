// Monkey patch the Array class and add a my_inject method. If my_inject receives
// no argument, then use the first element of the array as the default accumulator.

// write Array.prototype.myReduce (analogous to Ruby's Array#inject).

Array.prototype.myInject = function (accum, callback) {
  if (typeof accum === "undefined") {
    accum = this[0];
    var i = 1;
  } else {
    i = 0;
  }

  for (i ; i < this.length; i++) {
    accum = callback(accum, this[i]);
  }

  return accum;
};


Array.prototype.myReduce = function (func, acc) {
  if (acc === undefined) {
    acc = this[0];
    var i = 1;
  } else {
    i = 0;
  }
  for (i; i < this.length; i++) {
    acc = func(this[i], acc);
  }
  return acc;
};

Array.prototype.myReduce = function(callback) {
  let accum = this[0];

  this.slice(1).forEach((el) => {
    accum = callback(accum, el);
  });

  return accum;
};

// Array#myInject
Array.prototype.myReduce = function (func, initialValue) {

  let arr = this;

  if (!initialValue) {
    initialValue = arr[0];
    arr = arr.slice(1);
  }

  let result = initialValue;

  arr.myEach(el => result = func(result, el));

  return result;
};

console.log(NUMS.myReduce( (total, item) => total + item ));
