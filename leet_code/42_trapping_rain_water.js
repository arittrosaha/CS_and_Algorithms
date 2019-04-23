// Given n non - negative integers representing an elevation map where the width of each bar is 1, 
// compute how much water it is able to trap after raining.

// The above elevation map is represented by array[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1].In this case, 
// 6 units of rain water(blue section) are being trapped.Thanks Marcos for contributing this image!

// Example:
// Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
// Output: 6

/**
 * @param {number[]} height
 * @return {number}
 */

var trap = function (height) {
    let totalRain = 0;

    let i = 1;
    while (i < height.length) {
        if (height[i] < height[i-1]) {
            let [rainVolume, j] = checkTrapLtoR(i-1, height);
            if (j) i = j;
            if (rainVolume > -1) {
                totalRain += rainVolume;
            }
        }
        i += 1
    }

    let heightReversed = height.reverse();
    i = 1;
    while (i < heightReversed.length) {
        if (heightReversed[i] < heightReversed[i-1]) {
            let [rainVolume, j] = checkTrapRtoL(i-1, heightReversed);
            if (j) i = j;
            if (rainVolume > -1) {
                totalRain += rainVolume;
            }
        }
        i += 1
    }

    return totalRain;
};

function checkTrapLtoR (leftWallPos, height) {
    let land = 0;
    for (let i = leftWallPos+1; i < height.length; i++) {
        if (height[i] >= height[leftWallPos]) {
            land += 2 * Math.min(height[leftWallPos], height[i]);
            let totalArea = height[leftWallPos] * (i - (leftWallPos-1)); 
            let rain = totalArea - land;
            return [rain, i];
        }
        land += height[i];
    }
    return [-1];
}

function checkTrapRtoL (RightWallPos, height) {
    let land = 0;
    for (let i = RightWallPos+1; i < height.length; i++) {
        if (height[i] > height[RightWallPos]) {
            land += 2 * Math.min(height[RightWallPos], height[i]);
            let totalArea = height[RightWallPos] * (i - (RightWallPos-1)); 
            let rain = totalArea - land;
            return [rain, i];
        }
        land += height[i];
    }
    return [-1];
}

array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
// array = [4,2,3];
console.log(trap(array));