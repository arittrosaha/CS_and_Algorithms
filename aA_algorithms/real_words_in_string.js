// Returns an array of all the subwords of the string that appear in the
// dictionary argument. The method does NOT return any duplicates.

String.prototype.realWordsInString = function (dictionary) {
  let subWords = [];

  for (var i = 0; i < this.length; i++) {
    for (var j = i+1; j <= this.length; j++) {
      subWords.push(this.slice(i,j));
    }
  }

  let realWords = [];
  subWords.forEach( word => {
    if (dictionary.include(word)) {
      realWords.push(word);
    }
  });

  return realWords;
};

String.prototype._realWordsInString = function(dictionary) {
  let realWords = [];
  let result = [];

  dictionary.forEach( (el) => {
    if (this.includes(el)) result.push(el);
  });
  return result.sort();
};

String.prototype.realWordsInString = function (dictionary) {
  let realWords = [];
  for (let i = 0; i < this.length; i++) {
    let first = i;
    for (let j = 0; j < this.length; j++) {
      let last = j;
      let word = this.slice(first, last);

      if (dictionary.indexOf(word) > -1) {
        if (realWords.indexOf(word) < 0) realWords.push(word);
      }
    }
  }

  return realWords;
};
