function transpose(arr) {

};


// Array#transpose
Array.prototype.transpose = function() {

  // this creates the empty transposed array
  // just a neat trick to avoid iterating
  const columns = Array.from(
    { length: this[0].length },
    () => Array.from({ length: this.length })
  );

  for (let i = 0; i < this.length; i++) {
    for (let j = 0; j < this[i].length; j++) {
      columns[j][i] = this[i][j];
    }
  }

  return columns;
};

console.log([[0, 1, 2], [3, 4, 5], [6, 7, 8]].transpose());
