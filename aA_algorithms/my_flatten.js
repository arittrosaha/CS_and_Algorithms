Array.prototype.flatten = function () {
  let flattened = [];
  for (var i = 0; i < this.length; i++) {
    if (this[i].constructor.name === 'Array') {
      flattened = flattened.concat(this[i].flatten());
    } else {
      flattened.push(this[i]);
    }
  }
  return flattened;
};

Array.prototype.flatten = function () {
  let flattened = [];

  this.forEach( (el) => {
    if (el instanceof Array) {
      flattened = flattened.concat(el.flatten());
    } else {
      flattened.push(el);
    }
  });

  return flattened;
};
