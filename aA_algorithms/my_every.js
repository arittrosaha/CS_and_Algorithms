Array.prototype.myEvery = function (func) {
  for (var i = 0; i < this.length; i++) {
    if (!func(this[i])) {
      return false;
    }
  }
  return true;
};

Array.prototype.myEvery = function (func) {
  for (let i = 0; i < this.length; i++) {
    if (!func(this[i])) return false;
  }

  return true
}
