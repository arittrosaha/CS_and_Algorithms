// Given two words (beginWord and endWord), and a dictionary's word list,
// find the length of shortest transformation sequence from beginWord to endWord,
// such that:
//
// Only one letter can be changed at a time.
// Each transformed word must exist in the word list. Note that beginWord is
// not a transformed word.
//
// Note:
// Return 0 if there is no such transformation sequence.
// All words have the same length.
// All words contain only lowercase alphabetic characters.
// You may assume no duplicates in the word list.
// You may assume beginWord and endWord are non-empty and are not the same.
//
// Example 1:
// Input:
// beginWord = "hit",
// endWord = "cog",
// wordList = ["hot","dot","dog","lot","log","cog"]
//
// Output: 5
//
// Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
// "dog" -> "cog", return its length 5.
//
// Example 2:
// Input:
// beginWord = "hit"
// endWord = "cog"
// wordList = ["hot","dot","dog","lot","log"]
//
// Output: 0
//
// Explanation: The endWord "cog" is not in wordList, therefore no possible
// transformation.

/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */

function ladderLength(beginWord, endWord, wordList) {
	if (!wordList.includes(endWord)) return 0;

	let adj = adjList(beginWord, wordList);

	let beginFrontier = [beginWord];
	let beginVisited = new Set([beginWord]);

	let endFrontier = [endWord];
	let endVisited = new Set([endWord]);

	let turn = true;
	let numTurns = 1;

	while (beginFrontier.length || endFrontier.length) {
		numTurns++;

		if (turn) {
			expand(beginFrontier, beginVisited, adj);
		} else {
			expand(endFrontier, endVisited, adj);
		}

		if (hasIntersection(beginVisited, endVisited)) return numTurns;

		turn = !turn;
	}

	return 0;
}

function expand(frontier, visited, adj) {
	let newFrontier = [];
	while (frontier.length) {
		let node = frontier.pop();
		let neighbors = adj[node].filter(neighbor => !visited.has(neighbor));
		neighbors.forEach((neighbor) => visited.add(neighbor));
		newFrontier.push(...neighbors);
	}
	frontier.push(...newFrontier);
}

function hasIntersection(setA, setB) {
	var _intersection = new Set();
	for (var elem of setB) {
		if (setA.has(elem)) {
			_intersection.add(elem);
		}
	}
	return _intersection.size > 0;
}

function adjList(beginWord, wordList) {
	let neighbors = {};

	[beginWord, ...wordList].forEach(word => {
		neighbors[word] = wordList.filter(neighbor => oneDiff(word, neighbor));
	});

	return neighbors;
}

function oneDiff(word1, word2) {
	let numDiffs = 0;

	for (let i = 0; i < word1.length; i++) {
		if (word1[i] !== word2[i]) numDiffs++;
	}

	return numDiffs === 1;
}

console.log(ladderLength("a", "c", ["a","b","c"]));
