// write myFind(array, callback). It should return the first element for which
// callback returns true, or undefined if none is found.








Array.prototype.myFind = function (array, callback) {
  for (var i = 0; i < array.length; i++) {
    if (callback(array[i])) {
      return array[i];
    }
  }
  return undefined;
};




function myFind (array, callback) {
  for (let i = 0; i < array.length; i++) {
    if (callback(array[i])) {
      return array[i];
    }
  }
}
