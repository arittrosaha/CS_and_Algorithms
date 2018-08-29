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

caller();
