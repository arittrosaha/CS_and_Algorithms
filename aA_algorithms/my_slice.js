// write String.prototype.mySlice. It should take a start index and an
// (optional) end index.

String.prototype.mySlice = function (start, end) {

  if (typeof end === 'undefined') {
    end = this.length;
  }

  const sliced = '';

  for (var i = start; i < end && i < this.length; i++) {
    sliced += this[i];
  }
  return sliced;
};


String.prototype.mySlice = function (start, end) {
  let sliced = "";

  if (end === undefined) {
    end = this.length;
  }

  for (var i = start; i < end && i < this.length; i++) {
    sliced += this[i];
  }

  return sliced;
};

String.prototype.mySlice = function (start, end) {
  let slice = "";

  if (typeof end === 'undefined') {
    end = this.length;
  }

  for (let i = start; i < end && i < this.length; i++) {
    slice += this[i];
  }
  return slice;
};
