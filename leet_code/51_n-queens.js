// The n - queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens 
// attack each other.

// Given an integer n, return all distinct solutions to the n - queens puzzle.

// Each solution contains a distinct board configuration of the n - queens' placement, where 'Q' and 
// '.' both indicate a queen and an empty space respectively.

// Example:
// Input: 4
// Output: [
//     [".Q..",  // Solution 1
//         "...Q",
//         "Q...",
//         "..Q."],

//     ["..Q.",  // Solution 2
//         "Q...",
//         "...Q",
//         ".Q.."]
// ]

// Explanation: There exist two distinct solutions to the 4 - queens puzzle as shown above.

/**
 * @param {number} n
 * @return {string[][]}
 */

var solveNQueens = function (n) {
    let board = makeBoard(n);

    let solutions = recursive(board, new Set());

    return render(solutions);
};

function recursive (board, solutions) {
    if (checkQueens(board) && !(solutions.has(JSON.stringify(board)))) {
        solutions.add(JSON.stringify(board));
        return;
    }

    let n = board.length;

    for (let j = 0; j < n; j++) {
        for (let i = 0; i < n; i++) {
            if (board[j][i] === ".") {
                let newBoard = deepDup(board);
                newBoard[j][i] = "Q";
                let newestPos = [i, j];
                newBoard = updateBoard(newBoard, newestPos);
                recursive (newBoard, solutions)
            }
        }
    }

    return solutions;
}

function checkFull (board) {
    let n = board.length;

    for (let j = 0; j < n; j++) {
        for (let i = 0; i < n; i++) {
            if (board[j][i] === ".") {
                return false
            }
        }
    }

    return true;
}

function checkQueens (board) {
    let n = board.length;
    let counter = 0;

    for (let j = 0; j < n; j++) {
        for (let i = 0; i < n; i++) {
            if (board[j][i] === "Q") {
                counter += 1;
            }
        }
    }

    return counter === n;
}

function updateBoard (board, newestPos) {
    let [x, y] = newestPos;
    let newBoard = deepDup(board);
    let n = board.length;

    // vertical
    for (let j = 0; j < n; j++) {
        if (newBoard[j][x] === ".") {
            newBoard[j][x] = "x";
        } 
    }

    // horizontal
    for (let i = 0; i < n; i++) {
        if (newBoard[y][i] === ".") {
            newBoard[y][i] = "x";
        }
    }

    // Top left diagonal
    newBoard = markDiagPos(x, y, newBoard, ["-", "-"])

    // Bottom right diagonal
    newBoard = markDiagPos(x, y, newBoard, ["+", "+"])
    
    // Bottom left diagonal
    newBoard = markDiagPos(x, y, newBoard, ["-", "+"])
    
    // Top right diagonal
    newBoard = markDiagPos(x, y, newBoard, ["+", "-"])

    return newBoard;
}

function markDiagPos (x, y, board, signs) {
    let n = board.length;
    let newBoard = deepDup(board);

    directions = {
        "-" : -1,
        "+" : 1
    }
    
    signsJoined = signs.join("");

    let i = x + directions[signs[0]];
    let j = y + directions[signs[1]];
    while (conditionals(i, j, signsJoined, n)) {
        if (newBoard[j][i] === ".") {
            newBoard[j][i] = "x";
        }
        i = i + directions[signs[0]];
        j = j + directions[signs[1]];
    }

    return newBoard;
}

function conditionals (i, j, signs, n) {
    let boolean;

    if (signs === "--") {
        boolean = (i >= 0 && j >= 0);
    } else if (signs === "++") {
        boolean = (i < n && j < n);
    } else if (signs === "-+") {
        boolean = (i >= 0 && j < n);
    } else if (signs === "+-") {
        boolean = (i < n && j >= 0);
    }

    return boolean;
}


function makeBoard(n) {
    let board = [];

    for (let j = 0; j < n; j++) {
        let row = [];
        for (let i = 0; i < n; i++) {
            row.push(".")
        }
        board.push(row);
    }

    return board;
}

function render(solutions) {
    let results = [];

    solutions.forEach(solution => {
        let board = JSON.parse(solution);

        let stringBoard = [];

        board.forEach((row, idx) => {
            let stringRow = "";
            row.forEach(position => {
                if (position === "Q") {
                    stringRow += position;
                } else {
                    stringRow += ".";
                }
            });
            stringBoard.push(stringRow);
        });

        results.push(stringBoard);
    });

    return results;
}

function deepDup (array, newArray = []) {
    if (!Array.isArray(array)) return array;
    return array.map(el => deepDup(el));
}



// Chao's version

var solveNQueens2 = function (n) {
    let result = [];

    // Create 2-D array, and fill with "."
    let arr = new Array(n);
    for (let i = 0; i < arr.length; i++) {
        arr[i] = new Array(n);
        arr[i].fill(".");
    }

    let notDanger = function (board, row, col) {
        // check the same column before current row
        for (let i = 0; i < row; i++) {
            if (board[i][col] === "Q") return false;
        }
        // check diagonal before current row (from current to upper left)
        for (let i = row, j = col; i > 0 && j > 0; i-- , j--) {
            if (board[i - 1][j - 1] === "Q") return false;
        }
        // check diagonal before current row (from current to upper right)
        for (let i = row, j = col; i > 0 && j < n - 1; i-- , j++) {
            if (board[i - 1][j + 1] === "Q") return false;
        }
        return true;
    };

    function queen(array, row) {
        let temp = array.slice();
        // if row is greater than the index of last row, push result
        if (row === n) {
            for (let i = 0; i < temp.length; i++) {
                temp[i] = temp[i].join("");
            }
            result.push(temp);
        } else {
            for (let i = 0; i < n; i++) {
                if (notDanger(temp, row, i)) {
                    for (let j = 0; j < n; j++) {
                        array[row][j] = ".";
                    }
                    temp[row][i] = "Q";
                    queen(temp, row + 1);
                }
            }
        }
    }
    queen(arr, 0);
    return result;
};



// Dan's version

function makeBoard(num) {
    const board = [];
    for (let i = 0; i < num; i++) {
        board.push(new Array(num).fill(null));
    }
    return board;
}

function deepDupBoard(board) {
    let duppedBoard = board.map(row => {
        return row.slice(0);
    });
    return duppedBoard;
}

function fillOutBoard(board) {
    for (var i = 0; i < board.length; i++) {
        let row = board[i];
        for (var j = 0; j < row.length; j++) {
            if (row[j] !== "Q") row[j] = ".";
        }
    }
}

function placePiece(board, pos) {
    for (let i = pos[0]; i < board.length; i++) {
        let row = board[i];
        let j;
        if (i === pos[0]) {
            j = pos[1];
        } else {
            j = 0;
        }
        while (j < row.length) {
            let square = row[j];
            if (!square) {
                let copy = deepDupBoard(board);
                board[i][j] = "Q";
                plotMoves(board, [i, j]);
                if (row.length - 1 === j) {
                    j = 0;
                    i++;
                } else {
                    j++;
                }
                let nextPos = [i, j];
                return [board, nextPos, copy];
            }
            j++;
        }
    }
    return [null, null, null];
}

function plotMoves(board, pos) {
    movementUp(board, pos);
    movementDown(board, pos);
    movementLeft(board, pos);
    movementRight(board, pos);
    movementDiagonalRightUp(board, pos);
    movementDiagonalLeftUp(board, pos);
    movementDiagonalLeftDown(board, pos);
    movementDiagonalRightDown(board, pos);

    function movementUp(board, pos) {
        let [x, y] = [pos[0], pos[1]];
        if (board[x] === undefined) return;
        if (board[x][y] !== "." && board[x][y] !== "Q") board[x][y] = ".";
        let nextSquare = [x - 1, y];
        movementUp(board, nextSquare);
    }

    function movementDown(board, pos) {
        let [x, y] = [pos[0], pos[1]];
        if (board[x] === undefined) return;
        if (board[x][y] !== "." && board[x][y] !== "Q") board[x][y] = ".";
        let nextSquare = [x + 1, y];
        movementDown(board, nextSquare);
    }

    function movementLeft(board, pos) {
        let [x, y] = [pos[0], pos[1]];
        if (board[x][y] === undefined) return;
        if (board[x][y] !== "." && board[x][y] !== "Q") board[x][y] = ".";
        let nextSquare = [x, y - 1];
        movementLeft(board, nextSquare);
    }

    function movementRight(board, pos) {
        let [x, y] = [pos[0], pos[1]];
        if (board[x][y] === undefined) return;
        if (board[x][y] !== "." && board[x][y] !== "Q") board[x][y] = ".";
        let nextSquare = [x, y + 1];
        movementRight(board, nextSquare);
    }

    function movementDiagonalRightUp(board, pos) {
        let [x, y] = [pos[0], pos[1]];
        if (board[x] === undefined || board[x][y] === undefined) return;
        if (board[x][y] !== "." && board[x][y] !== "Q") board[x][y] = ".";
        let nextSquare = [x - 1, y + 1];
        movementDiagonalRightUp(board, nextSquare);
    }

    function movementDiagonalLeftUp(board, pos) {
        let [x, y] = [pos[0], pos[1]];
        if (board[x] === undefined || board[x][y] === undefined) return;
        if (board[x][y] !== "." && board[x][y] !== "Q") board[x][y] = ".";
        let nextSquare = [x - 1, y - 1];
        movementDiagonalLeftUp(board, nextSquare);
    }

    function movementDiagonalLeftDown(board, pos) {
        let [x, y] = [pos[0], pos[1]];
        if (board[x] === undefined || board[x][y] === undefined) return;
        if (board[x][y] !== "." && board[x][y] !== "Q") board[x][y] = ".";
        let nextSquare = [x + 1, y - 1];
        movementDiagonalLeftDown(board, nextSquare);
    }

    function movementDiagonalRightDown(board, pos) {
        let [x, y] = [pos[0], pos[1]];
        if (board[x] === undefined || board[x][y] === undefined) return;
        if (board[x][y] !== "." && board[x][y] !== "Q") board[x][y] = ".";
        let nextSquare = [x + 1, y + 1];
        movementDiagonalRightDown(board, nextSquare);
    }
}

// recursive go
var solveNQueens3 = function (n) {
    let board = makeBoard(n);
    let answers = [];
    if (n === 0) {
        return [];
    } else {
        placeQueens(n, board);
    }

    function placeQueens(n, board, queens = 0, pos = [0, 0]) {
        let dup;
        [board, pos, dup] = placePiece(board, pos);
        if (!board) {
            return;
        }
        let currentQueens = queens + 1;
        if (currentQueens === n) {
            fillOutBoard(board);
            board = board.map(row => {
                return row.join("");
            });
            board.join(",");
            answers.push(board);
        } else {
            placeQueens(n, board, currentQueens, pos);
        }
        placeQueens(n, dup, queens, pos);
        return;
    }
    return answers;
};

