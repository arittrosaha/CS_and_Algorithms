
function sum(arr) {
  if (!arr.length) return 0;

  let ele = arr.shift();
  return ele + sum(arr);
}

console.log(sum([1,2,3,4]));

// function weave(arr1, arr2) {
//   if (!arr2.length) return [ arr1 ];
//
//   let ele = arr2[0];
//   let insertions = [];
//   for (var i = 0; i <= arr1.length; i++) {
//     let left = arr1.slice(0, i);
//     let right = arr1.slice(i);
//     let restWeaves = weave(right, arr2.slice(1));
//     restWeaves.forEach(rest => {
//       insertions.push([ ...left, ele, ...rest ]);
//     });
//   }
//
//   return insertions;
// }

// function weave(arr1, arr2) {
//   if (!arr2.length) return [ arr1 ];
//
//   let ele = arr2.shift();
//   let insertions = [];
//   for (var i = 0; i <= arr1.length; i++) {
//     let left = arr1.slice(0, i);
//     let right = arr1.slice(i);
//     let restWeaves = weave(right, arr2);
//     restWeaves.forEach(rest => {
//       insertions.push([ ...left, ele, ...rest ]);
//     });
//   }
//
//   return insertions;
// }


// console.log(weave([1,2], ['a', 'b']));
// [ [ 'a', 'b', 1, 2 ],
//   [ 'a', 1, 'b', 2 ],
//   [ 'a', 1, 2, 'b' ],
//   [ 1, 'a', 'b', 2 ],
//   [ 1, 'a', 2, 'b' ],
//   [ 1, 2, 'a', 'b' ] ]
