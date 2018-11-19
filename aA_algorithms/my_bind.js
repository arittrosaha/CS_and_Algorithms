Function.prototype.myBind = function (ctx, ...bindArgs) {
  return (...callArgs) => {
    this.apply(ctx, bindArgs.concat(callArgs));
  };
};

















// write Function.prototype.myBind.
Function.prototype.myBind = function (ctx, ...bindArgs) {
  return (...callArgs) => this.apply(ctx, bindArgs.concat(callArgs));
};


// simple myBind with no args
Function.prototype.myBind = function (ctx) {
  return () => this.apply(ctx);
};

// myBind with arguments
Function.prototype.myBind = function (ctx, ...bindArgs) {
  return (...callArgs) => {
    return this.apply(ctx, bindArgs.concat(callArgs));
  };
};

class Cat {
  constructor(name) {
    this.name = name;
  }

  meow() {
    console.log(`${this.name} says meow!`);
  }
}

const curie = new Cat("Curie");
setTimeout(curie.meow.myBind(curie), 1000);
