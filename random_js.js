// spread and rest operator

function sayHello(first, last, ...otherArgs) { // resting
  console.log(first);
  console.log(last);
  console.log(otherArgs);
  console.log(...otherArgs); // spreading
}

// spread - when we use ... infront of an array argument, we are unpacking th elements (removing the bracket).
// rest - when we use ... infront of a parameter we, accept all arguments into that param.

sayHello("alvin", "zablan", "ny", "brooklyn", "11211");
