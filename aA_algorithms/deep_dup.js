// Using recursion and the is_a? method,
// write an Array#deep_dup method that will perform a "deep" duplication of the interior arrays.

function deepDup(arr) {
  return arr.map( el => el instanceof Array ? deepDup(el) : el);
}




function deepDup(arr) {
  return arr.map( (el) => el.constructor.name === 'Array' ? deepDup(el) : el);
}

// deepDup

// This function is a type-checking helper function
// See this article for an explanation:
// https://toddmotto.com/understanding-javascript-types-and-reliable-type-checking/
function getType(el) {
  return Object.prototype.toString.call(el).slice(8, -1);
}

function deepDup(arr) {
  if (getType(arr) !== 'Array') {
    return arr;
  }
  return arr.map((el) => {
    return deepDup(el);
  });
}

const array = [[2],3];
const dupedArray = deepDup(array);
console.log(`deepDup original = ${JSON.stringify(array)}`);

dupedArray[0].push(4);

console.log(`deepDup original = ${JSON.stringify(array)} (should not be mutated)`);
console.log(`deepDup duped = ${JSON.stringify(dupedArray)} (should be mutated)`);
