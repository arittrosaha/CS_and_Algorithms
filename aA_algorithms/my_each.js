Array.prototype.myEach = function (callback) {
  for (var i = 0; i < this.length; i++) {
    callback(this[i]);
  }
};












const NUMS = [1, 2, 3, 4, 5];

// Array#myEach
Array.prototype.myEach = function (func) {
  for (let i = 0; i < this.length; i++) {
    func(this[i]);
  }
};

NUMS.myEach((num) => {
  console.log(`square of ${num} is ${num * num}`);
});
