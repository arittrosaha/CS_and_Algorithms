
Function.prototype.myApply = function (ctx, args) {
  return this.bind(ctx, ...args)();
};













Function.prototype.myApply = function (ctx, args) {
  return this.bind(ctx, ...args)();
};
