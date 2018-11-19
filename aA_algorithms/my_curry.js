Function.prototype.myCurry = function (numArgs) {
  const args = [];
  const that = this;
  return function _curry(arg) {
    args.push(arg);
    if (args.length < numArgs) {
      return _curry;
    } else {
      return that(...args);
    }
  };
};

Function.prototype.myCurry = function (numArgs) {
  let argBalls = [];
  let fcn = this;
  return function _myCurry (el) {
    argBalls.push(el);
    if (argBalls.length < numArgs) {
      return _myCurry;
    } else {
      return fcn(...argBalls);
    }
  };
};
