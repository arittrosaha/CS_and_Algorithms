// Objects, Arrays, etc.. are pass by reference
//    meaning when you pass it as an arg, you are givin the exact
//    object in memory.

// Primitive types: nums, strings, bools... are pass by value
//    meaning when you pass it as an arg, you are giving a copy of
//    the value.


function callee(array) {
  array.push('stuff');
}

function caller() {
  var arr = [];
  callee(arr);
  console.log(arr);
}

// caller();


// spread and rest operator

function sayHello(first, last, ...otherArgs) { // resting
  console.log(first);
  console.log(last);
  console.log(otherArgs);
  console.log(...otherArgs); // spreading
}

// spread - when we use ... infront of an array argument, we are unpacking th elements (removing the bracket).
// rest - when we use ... infront of a parameter we, accept all arguments into that param.

// sayHello("alvin", "zablan", "ny", "brooklyn", "11211");

// Generator function

function* myGenerator() {
  console.log('first');
  yield 42;
  console.log('second');
  yield 100;
}

let gen = myGenerator();
// console.log(gen.next());
// console.log(gen.next());

// for...of loop
// of calls next() for a Iterator Object

for (let thing of gen) {
  console.log(thing);
}

// for..in loop
// in can be used to iterate through only POJO


// function within the function; closure
function makeCounter(num){
  var i = num;

  function count() {
    console.log(i); // i is closed over
    i++;
  }

  return count;
}
