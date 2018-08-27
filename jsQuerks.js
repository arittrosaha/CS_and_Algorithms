// IFFE:

// Immediately Invoked Function Expression
(function () {
  console.log("hi");
  // your code
})();


// Hoisting:

sayHello1(); // # => hi
// this def is hoisted (pushed to the very top)
function sayHello1() {
  console.log('hi');
}

sayHello2(); // # => undefined
// only declaration (var sayHello2) is hoisted but not the function assignment
var sayHello2 = function() {
  console.log('hello world');
};

// only var declaration are hoisted, not the declaration portion.
console.log(bootcamp);
var bootcamp; // this is just a declaration
bootcamp = 'hi'; // this is an assignment

// const and let declarations are not hoisted.


function myFunc1() {
  return {
    "a": "stuff"
  };
}

function myFunc2() {
  return // js implicitly adds a ; at the end of this return which will seperate the return from the rest of the code below.
  (
    {
      "a": "stuff"
    }
  )
}


console.log((function f(name) {
  console.log('I am ' + name);
})('alvin')); // works fine

console.log(f); // prints the type of input which is Function here.
console.log(String(f)); // prints the function in string format.
console.log(String(console.log)); // blocks the string print of native code.
