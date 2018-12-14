// Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 
// 1's and return its area.

// Example:

// Input:
// 1 0 1 0 0
// 1 0 1 1 1
// 1 1 1 1 1
// 1 0 0 1 0

// Output: 4

/**
 * @param {character[][]} matrix
 * @return {number}
 */

// Dan's solution
var maximalSquare1 = function (matrix) {
    let max = 0;
    for (let i = 0; i < matrix.length; i++) {
        let row = matrix[i];
        for (var j = 0; j < row.length; j++) {
            let num = row[j];
            if (num === "0") continue;
            let limit = 0;

            while (checkIfSquare(matrix, [i, j], limit)) {
                let possibleMax = (limit + 1) * (limit + 1);
                if (max < possibleMax) {
                    max = possibleMax;
                }
                limit++;
            }
        }
    }
    return max;
};

function checkIfSquare(matrix, startPos, limit, checked) {
    const row = startPos[0];
    const col = startPos[1];
    for (let i = row; i <= row + limit; i++) {
        let subArray = matrix[i];
        if (!subArray) return false;

        for (let j = col; j <= col + limit; j++) {
            let el = subArray[j];
            if (!el || el === "0") return false;
        }
    }
    return true;
}

// Chao's solution
var maximalSquare2 = function (matrix) {
    if (!matrix.length) return 0;
    let squareLen = 0;
    let rowLen = matrix.length;
    let colLen = matrix[0].length;

    let arr = new Array(rowLen + 1);
    for (let i = 0; i < arr.length; i++) {
        arr[i] = new Array(colLen + 1);
        arr[i].fill(0);
    }

    for (let i = 1; i <= rowLen; i++) {
        for (let j = 1; j <= colLen; j++) {
            if (matrix[i - 1][j - 1] === "1") {
                arr[i][j] =
                    Math.min(Math.min(arr[i][j - 1], arr[i - 1][j]), arr[i - 1][j - 1]) +
                    1;
                squareLen = Math.max(arr[i][j], squareLen);
            }
        }
    }

    return squareLen * squareLen;
};