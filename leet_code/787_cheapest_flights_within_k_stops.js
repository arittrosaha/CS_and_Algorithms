// There are n cities connected by m flights.Each fight starts from city u and arrives at v with a price w.
// Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops.If there is no such route, output - 1.

// Example 1:
// Input:
// n = 3, edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
// src = 0, dst = 2, k = 1
// Output: 200
// Explanation:
// The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
    
// Example 2:
// Input:
// n = 3, edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
// src = 0, dst = 2, k = 0
// Output: 500
// Explanation:
// The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

// Note:
// The number of nodes n will be in range[1, 100], with nodes labeled from 0 to n - 1.
// The size of flights will be in range[0, n * (n - 1) / 2].
// The format of each flight will be(src, dst, price).
// The price of each flight will be in the range[1, 10000].
// k is in the range of[0, n - 1].
// There will not be any duplicated flights or self cycles.

/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} K
 * @return {number}
 */

var findCheapestPrice = function(n, flights, src, dst, K) {};

function minPath(node, dest, adj, k) {
    if (node === dest) return 0;
    if (k === 1) return -1;

    let neighbours = adj[node];
    let options = [];

    for (let n in neighbours) {
        let result = minPath(n, dest, adj, k-1);
        if (result > -1) options.push(result + neighbours[n]);
    }

    return Math.min(options);
}

// todo:
// - build adj list
// - hand inner cycles

// Alvin's solution
function findCheapestPrice1(n, flights, src, dst, k) {
  let adj = buildAdjList(flights);
  let minCost = { [src]: 0 };
  let queue = [src];
  let pathSize = 0;
  while (pathSize <= k) {
    let newNodes = [];
    let newMinCost = {};
    while (queue.length) {
      let node = queue.pop();
      let costs = adj[node];
      for (let neighbor in costs) {
        let thisCost = minCost[node] + costs[neighbor];
        if (
          thisCost < newMinCost[neighbor] ||
          newMinCost[neighbor] === undefined
        ) {
          newMinCost[neighbor] = thisCost;
          newNodes.push(neighbor);
        }
      }
    }
    for (let n in newMinCost) {
      if (newMinCost[n] < minCost[n] || minCost[n] === undefined)
        minCost[n] = newMinCost[n];
    }
    queue.push(...Object.keys(newMinCost));
    pathSize++;
  }
  return minCost[dst] || -1;
}

function buildAdjList(flights) {
  let adj = {};
  flights.forEach(flight => {
    let [src, dst, cost] = flight;
    if (src in adj) {
      adj[src][dst] = cost;
    } else {
      adj[src] = { [dst]: cost };
    }
  });
  return adj;
}

// Chao's solution
var findCheapestPrice = function (n, flights, src, dst, K) {
  let dp = new Array(n);
  dp.fill(Infinity);
  dp[src] = 0;

  for (let i = 0; i <= K; i++) {
    let newDp = dp.slice();
    for (let j = 0; j < flights.length; j++) {
      newDp[flights[j][1]] = Math.min(newDp[flights[j][1]], dp[flights[j][0]] + flights[j][2]);
    }
    dp = newDp;
  }
  return dp[dst] === Infinity ? -1 : dp[dst];
};