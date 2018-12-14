// Given a non - empty array of integers, return the k most frequent elements.

// Example 1:
// Input: nums = [1, 1, 1, 2, 2, 3], k = 2
// Output: [1, 2]

// Example 2:
// Input: nums = [1], k = 1
// Output: [1]

// Note:
// - You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
// - Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

// var topKFrequent = function (nums, k) {
//     let topKElements = [];
//     let counts = counterHash(nums);

//     for (key in counts) {
        
//     }
// };

// function counterHash (array) {
//     let counter = {};
//     let 

//     for (let i = 0; i < array.length; i++) {
//         let currEl = array[i];
//         if (currEl in counter) {
//             counter[currEl] += 1;
//         } else {
//             counter[currEl] = 1;
//         }
//     }

//     return counter;
// }

// Chao's solution
var topKFrequent = function (nums, k) {
    if (nums.length === k) return nums;
    let freq = {};
    for (let i = 0; i < nums.length; i++) {
        if (!freq[nums[i]]) {
            freq[nums[i]] = 1;
        } else {
            freq[nums[i]]++;
        }
    }
    let keys = Object.keys(freq)
    if (keys.length === k) return keys;
    let arr = []
    for (let key in freq) {
        arr.push([key, freq[key]]);
    }

    arr = arr.sort((a, b) => b[1] - a[1]);

    let result = [];
    while (result.length < k) {
        result.push(Number(arr[result.length][0]));
    }

    return result;
};