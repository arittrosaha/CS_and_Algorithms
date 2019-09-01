function coinChange1(coins, amt, numCoins = 0, memo = {}) {
  let key = `[${coins}]-${amt}-${numCoins}`;
  // console.log(key);

  if (amt === 0) return numCoins;
  if (coins.length === 0) return -1;

  // let reducer = (accum, currVal) => accum + currVal;
  // if (coins.reduce(reducer, 0) > amt) return -1;

  if (key in memo) {
    return memo[key];
  }

  let coinVal = coins[coins.length -1];
  let possibilities = [];

  for (let quantity = 0; quantity <= (amt/coinVal); quantity++) {
    possibilities.push(
      coinChange1(coins.slice(0, -1), amt - (quantity * coinVal), numCoins + quantity, memo)
    );
  }

  let filtered = possibilities.filter((num) => num !== -1);
  console.log(filtered);

  if (filtered.length === 0) {
    memo[key] = -1;
    // console.log(`${key}, ${memo[key]}`);
    return -1;
  } else {
    let best = Math.min(...filtered);
    memo[key] = best;
    // console.log(`${key}, ${memo[key]}`);
    return best;
  }

}

console.log(coinChange1([1,2,5], 11));
console.log(coinChange1([3,7,405,436], 8839));


function coinChange2(coins, amt, memo={0: 0}) {
  if (amt < 0) return -1;
  if (amt in memo) return memo[amt];

  let coinCounts = coins
    .map(val => coinChange2(coins, amt - val, memo))
    .filter((count) => count !== -1)
    .map((count) => count + 1);

  if (!coinCounts.length) {
    memo[amt] = -1;
  } else {
    memo[amt] = Math.min(...coinCounts);
  }

  return memo[amt];
}


console.log(coinChange2([1,2,5], 11));
console.log(coinChange2([2], 3));

function coinChange3(coins, amount) {
  let max = amount + 1;
  let arr = new Array(amount + 1);

  arr.fill(max);
  arr[0] = 0;

  for (let i = 1; i <= amount; i++) {
    for (let j = 0; j < coins.length; j++) {
      if (coins[j] <= i) {
        arr[i] = Math.min(arr[i], arr[i - coins[j]] + 1);
      }
    }
  }

  return arr[amount] > amount ? -1 : arr[amount];
}
