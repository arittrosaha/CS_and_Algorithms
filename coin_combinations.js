function change (amt, coins, memo = {}) {
  let key = `${amt}-${coins.join(",")}`;

  if (key in memo) {
    return memo[key];
  }

  if (amt === 0) return 1;
  if (coins.length === 0) return 0;

  let coinVal = coins[coins.length - 1];
  // picking the biggest coin has better memory efficiency than picking the smallest coin
  let total = 0;
  for (let quantity = 0; quantity <= (amt / coinVal); quantity++) {
    total += change(amt - (quantity * coinVal), coins.slice(0, -1));
  }

  memo[key] = total;
  return total;
}

console.log(change(5, [1,2,5]));
console.log(change(11, [1,2,5]));
console.log(change(1000, [1,2,5]));


var changeLCS = function(amount, coins) { // leetcodesolution
  let arr = new Array(amount + 1);

  arr.fill(0);
  arr[0] = 1;

  coins.forEach(coin => {
    for (let i = coin; i <= amount; i++) {
      arr[i] += arr[i - coin];
    }
  });

  return arr[amount];
};
