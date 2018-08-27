function subsets(arr) {
  if (arr.length === 0) {
    return [[]];
  }

  let withoutFirst = subsets(arr.slice(1));
  let withFirst = withoutFirst.map((subset) => {
    return [arr[0], ...subset];
  });

  return [...withoutFirst, ...withFirst];
}
// let arr1 = ["a", "b", "c", "d"];
// console.log(subsets(array));



function permutations(arr){
  if (arr.length === 1) {
    return [arr];
  }

  let without = permutations(arr.slice(1));
  let allPerms = [];
  without.forEach((perm) => {
    for (let i = 0; i <= perm.length; i++) {
      let newPerm = [...perm.slice(0,i), arr[0], ...perm.slice(i)];
      allPerms.push(newPerm);
    }
  });

  return allPerms;
}

// let arr2 = ["a", "b", "c", "d", "e"];
// console.log(permutations(arr2).length);
