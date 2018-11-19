// Write a String#symmetric_substrings method that returns an array of substrings
// that are palindromes, e.g. "cool".symmetric_substrings => ["oo"]
// Only include substrings of length > 1.
String.prototype.symmetricSubstrings = function () {
  const symStrings = [];

  for (var i = 0; i < this.length; i++) {
    for (var j = i + 1; j <= this.length; j++) {
      let subString = this.slice(i,j);
      if (subString.split("").reverse().join("") === subString) {
        symStrings.push(subString);
      }
    }
  }
  return symStrings.filter( el => el.length !== 1 );
};
