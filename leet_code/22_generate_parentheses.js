function generateParenthesis(n) { // time: O(n!)
  if (n === 1) return ["()"];

  let prevCobminations = generateParenthesis(n - 1);
  let combinations = [];
  prevCobminations.forEach((comb) => {
    for (let i = 0; i <comb.length; i++) {
      combinations.push(comb.slice(0,i) + "()" + comb.slice(i));
    }
  });

  return Array.from(new Set(combinations));
}

console.log(generateParenthesis(3));
