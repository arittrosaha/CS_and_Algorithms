// Array#.myMap
Array.prototype.myMap = function (callback) {
  const mapped = [];
  for (var i = 0; i < this.length; i++) {
    mapped.push(callback(this[i]));
  }
  return mapped;
};


Array.prototype.myMap = function (callback) {
  const mapped = [];
  this.forEach( el => mapped.push(callback(el)));
  return mapped;
};

Array.prototype.myMap = function (callback) {
  const mapped = [];
  this.forEach(function (el) {
    mapped.push(callback([el]));
  });
  return mapped;
};


Array.prototype.myMap = function (func) {
  const mapped = [];
  this.forEach(el => mapped.push(func(el)));
  return mapped;
};

Array.prototype.myMap = function (func) {
  const mappedArray = [];

  this.myEach(element => mappedArray.push(func(element)) );

  return mappedArray;
};

console.log(NUMS.myMap( num => num * num ));
