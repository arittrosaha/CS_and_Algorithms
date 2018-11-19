Array.prototype.myFilter = function (callback) {
  const filtered = [];
  for (var i = 0; i < this.length; i++) {
    if (callback(this[i])) {
      filtered.push(this[i]);
    }
  }
  return filtered;
};











Array.prototype.myFilter = function (func) {
  let filtered = [];
  for (var i = 0; i < this.length; i++) {
    if (func(this[i])) {
      filtered.push(this[i]);
    }
  }
  return filtered;
};

[1,2,3,4,5].myFilter((el) => el % 2 === 0);

Array.prototype.myFilter = function (func) {
  const selection = [];
  this.forEach( (el) => {
    if (func(el)) selection.push(el);
  });

  return selection;
};
