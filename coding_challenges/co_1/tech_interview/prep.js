/*
Exercise Goal:
    - The goal of this exercise is to show us how you apply software engineering
    principles to create a maintainable software solution.

    How to approach this:

            - Don't worry about persistence. It would make sense here, but for this
            exercise only use in-memory data structures.
            - Don't worry about tricks or "gotchyas", as there aren't any.
            - Just focus on writing clean maintainable code.



Specification:

    Create a class LeaderBoard whose interface includes the following methods:

    Method Name: add_score

        - Add a new score to the player's average. If a player doesn't exist in the
        LeaderBoard, they will be automatically added.

        Args:

                player_id (Integer): The player's ID.
                score (Integer): The score to record for the player

        Returns:

                Double: The new average score for the given player

    Method Name: top

        - Get the top player_ids on the leaderboard ordered by their average scores
        from highest to lowest

        Args:

                num_players (Integer): The maximum number of player_ids to return

        Returns:

                List<Integer>: a list of player_ids

    Method Name: reset

        - Removes any scoring information for a player, effectively
        resetting them to 0

        Args:

                player_id (Integer): The player's ID.

Example Usage:


    // Create a new LeaderBoard Instance
    LeaderBoard leader_board = new LeaderBoard();

    // Add scores for players to the LeaderBoard
    leader_board.add_score(1, 50); // 50.0
    leader_board.add_score(2, 80); // 80.0
    leader_board.add_score(2, 70); // 75.0
    leader_board.add_score(2, 60); // 70.0
    leader_board.add_score(3, 90); // 90.0
    leader_board.add_score(3, 85); // 87.5

    // Get top positions for the leaderboard
    leader_board.top(3); // [3, 2, 1]
    leader_board.top(2); // [3, 2]
    leader_board.top(1); // [3]

    // Reset a player 3's scores
    leader_board.reset(3); // void

    // Player 3 is now at the bottom of the leaderboard
    leader_board.top(3); // [2, 1, 3]

Expected values

    - Player IDs will always be positive integers small enough to be
    stored as a signed 32-bit integer Scores are integers ranging from 0-100


We have provided stubbed out code and tests for you below. Please note that these tests are not exhaustive and do not cover all corner cases. We recommend extending the given tests to ensure your code is correct.

*/


// Your code goes here. Feel free to make helper classes if needed
class LeaderBoard {
    constructor() {
        this.count = {};
        this.board = {};
        this.average = {};
    }

    add_score(player_id, score, date) {
        if (this.count[player_id] === undefined) {
            this.count[player_id] = 1;
        } else {
            this.count[player_id]++;
        }

        let sum = 0;
        let scoreArr = [];
        let dateObj = {};
        if (this.board[player_id] === undefined) {
            scoreArr.push(dateObj[date] = score);
            this.board[player_id] = scoreArr;
        } else {
            this.board[player_id].push(dateObj[date] = score);
        }
        console.log(this.board);
        for (let i = 0; i < this.board[player_id].length; i++) {
            sum += this.board[player_id][i][date];
        }
        this.average[player_id] = sum / this.count[player_id];
        return this.average[player_id];
    };

    top(num_players) {
        let position = [];
        let newPos = [];

        for (let id in this.average) {
            position.push([id, this.average[id]]);
        }

        position.sort(function (a, b) {
            return b[1] - a[1];
        });

        for (let i = 0; i < num_players; i++) {
            let player_id = position[i][0];
            newPos.push(Number(player_id));
        }
        return newPos;
    };

    reset(player_id) {
        this.count[player_id] = 0;
        this.board[player_id] = 0;
        this.average[player_id] = 0;
    };

    findHighScore(date1, date2) {

    }
}

// Test code here

function array_equals(a, b) {
    if (a === b) return true;
    if (a == null || b == null) return false;
    if (a.length != b.length) return false;
    for (var i = 0; i < a.length; ++i) {
        if (a[i] !== b[i]) return false;
    }
    return true;
}

var leader_board = new LeaderBoard()

leader_board.add_score(1, 50, 5)
console.log(leader_board.add_score(2, 80, 4) == 80)
console.log(leader_board.add_score(2, 70, 3) == 75)
console.log(leader_board.add_score(2, 60, 2) == 70)
console.log('Add score should return the average. test with 1 score')
console.log(leader_board.add_score(3, 90, 10) == 90)
console.log('Add score should return the average. test with 2 scores')
console.log(leader_board.add_score(3, 85, 12) == 87.5)
console.log('Top 3 [' + leader_board.top(3) + '] should equal [3, 2, 1]:')
console.log(array_equals(leader_board.top(3), [3, 2, 1]))
console.log('Top 2 [' + leader_board.top(2) + '] should equal [3, 2]:')
console.log(array_equals(leader_board.top(2), [3, 2]))
leader_board.reset(3)
console.log('After reset top 3 [' + leader_board.top(3) + '] should equal [2, 1, 3]')
console.log(array_equals(leader_board.top(3), [2, 1, 3]))