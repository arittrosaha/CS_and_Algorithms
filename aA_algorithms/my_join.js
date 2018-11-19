Array.prototype.myJoin = function (separator) {
  let joined = "";
  for (var i = 0; i < (this.length-1); i++) {
    joined += this[i];
    joined += separator;
  }
  joined += this.slice(-1)[0];
  return joined;
};


Array.prototype.myJoin = function (separator = '') {
  let newString = '';

  this.forEach( (el, idx) => {
    newString += `${el}`;
    if (idx < this.length - 1) newString += separator;
  });

  return newString;
};
