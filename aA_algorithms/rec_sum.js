// Write a recursive method that returns the sum of all elements in an array

function recSum(nums) {
  if (nums.length === 1) {
    return nums[0];
  }

  let sum = recSum(nums.slice(1));
  sum += nums[0];
  return sum;
}


// sumRec
function sumRec(numbers) {
  if (numbers.length === 0) {
    return 0;
  }

  let lastNum = numbers[numbers.length - 1];
  return sumRec(numbers.slice(0, numbers.length - 1)) + lastNum;
}

console.log(`sumRec([1, 3, 5]) = ${sumRec([1, 3, 5])}`);

// sumIter
function sumIter(numbers) {
  let sum = 0;

  numbers.forEach(function (number) {
    sum += number;
  });

  // or use reduce
  const reducedSum = numbers.reduce((acc, el) => acc + el);

  return sum;
  // return reducedSum;
}

console.log(`sumIter([1, 3, 5]) = ${sumIter([1, 3, 5])}`);
